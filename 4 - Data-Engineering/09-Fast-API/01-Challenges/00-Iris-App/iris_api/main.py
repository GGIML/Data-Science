import pickle
import uuid
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client["iris_api"]
models_mg = db["models"]


MODELS = {
	"lr": {
		"name": "Logistic Regression",
		"api_model_code": "lr",
		"documentation": "https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html",
		"model": LogisticRegression
	},
	"dt": {
		"name": "Decision Tree",
		"api_model_code": "dt",
		"documentation": "https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html",
		"model": DecisionTreeClassifier
	},
	"knn": {
		"name": "K Nearest Neighbors",
		"api_model_code": "knn",
		"documentation": "https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html",
		"model": KNeighborsClassifier
	}
}

IRIS_TYPES = {
	0: 'setosa',
	1: 'versicolor',
	2: 'virginica'
}


app = FastAPI()


class ModelInfo(BaseModel):
	name: str
	api_model_code: str
	documentation: str = None

class ModelTrainIn(BaseModel):
	api_model_code: str
	trained_model_name: str


class ModelTrainOut(BaseModel):
	train_id: str = None
	api_model_code: str = None
	trained_model_name: str = None
	accuracy: float = None

class ModelIrisPredictIn(BaseModel):
	train_id: str
	sepal_length: float
	sepal_width: float
	petal_length: float
	petal_width : float

class ModelIrisPredictOut(BaseModel):
	type_predicted: str
	proba_setosa: float
	proba_versicolor: float
	proba_virginica: float
	train_id: str

@app.get("/")
async def root():
	return {"message": "Welcome to Iris ML API made by VIVA DATA!"}


@app.get("/model/info", response_model=List[ModelInfo])
async def info_models():
	result = []
	for model_key in MODELS:
		model_info = MODELS[model_key]
		model_info.pop("model")
		result.append(model_info)
	return result


@app.post("/model/train/", response_model=ModelTrainOut)
async def train_model(model_train: ModelTrainIn):
	model_train_dict = model_train.dict()
	model = MODELS[model_train_dict['api_model_code']]['model']()
	data = load_iris()
	X = data.data
	y = data.target
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, stratify=y, random_state=42)
	model.fit(X_train, y_train)
	y_pred = model.predict(X_test)
	accuracy = accuracy_score(y_test, y_pred)
	unique_id = uuid.uuid4().hex
	filename = f"trained_models/{unique_id}.sav"
	pickle.dump(model, open(filename, 'wb'))
	model_train_dict.update({"train_id": unique_id, "accuracy": accuracy})
	models_mg.insert_one(model_train_dict)
	return model_train_dict


@app.get("/model/list/", response_model=List[ModelTrainOut])
async def trained_models():
	result = models_mg.find({}, {"_id": 0})
	return list(result)


@app.get("/model/{train_id}", response_model=ModelTrainOut)
async def trained_models(train_id: str):
	result = models_mg.find_one({"train_id": train_id}, {"_id": 0})
	return result


@app.patch("/model/update/{train_id}", response_model=ModelTrainOut)
async def update_trained_model(train_id: str, model_train: ModelTrainOut):
	stored_model_train = models_mg.find_one({"train_id": train_id})
	stored_model_train = ModelTrainOut(**stored_model_train)
	update_data = model_train.dict(exclude_unset=True)
	updated_item = stored_model_train.copy(update=update_data)
	models_mg.update_one({"train_id": train_id}, {"$set": update_data})
	return updated_item


@app.post("/model/predict/", response_model=ModelIrisPredictOut)
async def predict_iris(iris_data: ModelIrisPredictIn):
	result = {}
	iris_data_dict = iris_data.dict()
	train_id = iris_data_dict['train_id']
	model = pickle.load(open(f"trained_models/{train_id}.sav", 'rb'))
	data = [
				[
					iris_data_dict['sepal_length'],
					iris_data_dict['sepal_width'],
					iris_data_dict['petal_length'],
					iris_data_dict['petal_width']
				]
			]
	pred = model.predict(data)[0]
	proba = model.predict_proba(data)[0]
	return {
		"type_predicted": IRIS_TYPES[pred],
		"proba_setosa": proba[0],
		"proba_versicolor": proba[1],
		"proba_virginica": proba[2],
		"train_id": train_id
	}
