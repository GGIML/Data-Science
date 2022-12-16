from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
import numpy as np
import uuid
import pickle
from typing import List

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

from datetime import datetime as dt

app = FastAPI()

client = MongoClient('localhost', 27017)
db = client['california_api']
models_mongo = db['models']

#
#Create a post method for the URL newcaliforniareg
#for creating a new trained regression model. On the parameters sent,
#indicate the proportion of data to be used for the training and the alpha
#for Ridge to be used. Remember you have to save this model using pickle
#and save the related information into MongoDB.
#

class ModelsTrainIn(BaseModel):
    train_size: float
    alpha: float

class ModelsTrainOut(BaseModel):
    model_name: str
    train_size: float
    alpha: float
    id: str
    timestamp: dt
    rse: float

class DataList(BaseModel):
    med_inc: float
    house_age: float
    ave_rooms: float
    ave_bedrms: float
    population: float
    ave_occup: float
    latitude: float
    longitude: float

class Predictions(BaseModel):
	price:float

@app.post('/newcaliforniareg', response_model=ModelsTrainOut)
async def train_model(model_params:ModelsTrainIn):
    model_train_dict = model_params.dict()
    train_size = model_train_dict['train_size']
    alpha = model_train_dict['alpha']

    data = fetch_california_housing()

    X = data.data
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_size)

    model = Ridge(alpha=alpha)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    rse = np.sum((y_test-y_pred)**2) / np.sum((y_test-y_test.mean())**2)

    unique_id = uuid.uuid4().hex

    # saving the model locally
    filename = f"trained_models/{unique_id}.sav"
    pickle.dump(model, open(filename, 'wb'))
    model_train_dict.update({"model_name": f"Ridge Regressor {alpha}", "id": unique_id, "rse": rse, "timestamp": dt.now()})

    # saving the information into MongoDB
    models_mongo.insert_one(model_train_dict)

    return model_train_dict

#Create a get method to list all trained models created.
@app.get("/model/list", response_model=List[ModelsTrainOut])
async def get_models_list():
    lst_models = models_mongo.find({}, {"_id":0})
    return list(lst_models)
    
@app.post("model/predict", response_model=Predictions)
def predict(data_list: DataList):
	
	model=pickle.load(open("trained_models/ea77d3ee92e94d0e8e21a2d06ca765f8.sav", 'rb'))
	data_list_dict = data_list.dict()
	data = [[value for key, value in data_list_dict.items()]]
	price = model.predict(data).round(2)
	
	return price
