import pickle
from flask import Flask, render_template, request
import requests



app = Flask(__name__)


@app.route('/', methods=['GET'])
def california_index():
    return render_template('index.html')

@app.route('/predict/', methods=['POST'])
def results():
	MedInc	= float(request.form['MedInc'])
	HouseAge = float(request.form['HouseAge'])
	AveRooms = float(request.form['AveRooms'])
	AveBedrms = float(request.form['AveBedrms'])
	Population = float(request.form['Population'])
	AveOccup = float(request.form['AveOccup'])
	Latitude = float(request.form['Latitude'])
	Longitude = float(request.form['Longitude'])

	r = requests.post("http://127.0.0.1:8000/model/predict/", json={
		"train_id": "0c0d129002c74bc5afb534c041d38e4e",
		"MedInc": MedInc,
		"HouseAge": HouseAge,
		"AveRooms": AveRooms,
		"AveBedrms": AveBedrms,
		"Population": Population,
		"AveOccup": AveOccup,
		"Latitude": Latitude,
		"Longitude": Longitude
  
	})
 
	api_response = r.json()
	return render_template('prediction.html', price=api_response['reg'])


if __name__ == '__main__':
    app.run(
		host='0.0.0.0',
  		port=5000,
  		debug=True
	)