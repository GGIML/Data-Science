# Imports
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error
import uuid
import pickle
import os
from typing import List

app = FastAPI()

class ModelTrainIn(BaseModel):
	alpha: float
	size: float
	name: str


class ModelTrainOut(BaseModel):
	alpha: float=None
	size: float=None
	name: str=None
	train_id: str=None
	mse: float=None
 
 
@app.get("/")
async def index():
    return {"API": "House Pricing" }
        

@app.post("/model/newcaliforniareg/", response_model=ModelTrainOut)
async def train_ridge(cal_hous_data: ModelTrainIn):
	cal_hous_dict = cal_hous_data.dict()
	alpha = cal_hous_dict['alpha']
	size = cal_hous_dict['size']
	name = cal_hous_dict['name']

	model = Ridge(alpha=alpha)
	data = fetch_california_housing()
	X = data.data
	y = data.target

	X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=size, random_state=42)

	model.fit(X_train, y_train)

	y_pred = model.predict(X_test)

	mse = mean_squared_error(y_test, y_pred)

	unique_id = uuid.uuid4().hex

	if not os.path.exists("trained_models"):
		os.makedirs("trained_models")

	pickle.dump(model, open(f"trained_models/{unique_id}.pkl", "wb"))

	cal_hous_dict.update({"train_id":unique_id, "mse": mse})

	return cal_hous_dict

class ModelPredictIn(BaseModel):
	train_id: str
	MedInc: float
	HouseAge: float
	AveRooms: float
	AveBedrms: float
	Population: float
	AveOccup: float
	Latitude: float
	Longitude: float


class ModelPredictOut(BaseModel):
	train_id: str
	reg: float
        

@app.post("/model/predict/", response_model=ModelPredictOut)
async def california_predict(query_data: ModelPredictIn):
	query_data_dict = query_data.dict()
	model_id = query_data_dict['train_id']
	model = pickle.load(open(f"trained_models/{model_id}.pkl", 'rb'))
	
	MedInc =  query_data_dict['MedInc']
	HouseAge = query_data_dict['HouseAge']
	AveRooms = query_data_dict['AveRooms']
	AveBedrms = query_data_dict['AveBedrms']
	Population = query_data_dict['Population']
	AveOccup = query_data_dict['AveOccup']
	Latitude = query_data_dict['Latitude']
	Longitude = query_data_dict['Longitude']

	reg = model.predict([[MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude, Longitude]])

	return {
		"reg": reg,
		"train_id": model_id
	}
 
 
