import pickle
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def california_index():
    return render_template('index.html')
    # TODO : complete function


@app.route('/predict/', methods=['POST'])
def result():
    med_inc = float(request.form["MedInc"])
    house_age = float(request.form["HouseAge"])
    ave_rooms = float(request.form["AveRooms"])
    ave_bedrms = float(request.form["AveBedrms"])
    population = float(request.form["Population"])
    ave_occup = float(request.form["AveOccup"])
    latitude = float(request.form["Latitude"])
    longitude = float(request.form["Longitude"])

    data = [[med_inc, house_age, ave_rooms, ave_bedrms, population, ave_occup, latitude, longitude]]

    model = pickle.load(open("../../../../08-Fast-API/01-Challenges/01-Build-your-API/california_housing_api/trained_models/ea77d3ee92e94d0e8e21a2d06ca765f8.sav", 'rb'))

    price = model.predict(data).round(2)

    return render_template('prediction.html', price=float(price))

if __name__ == '__main__':
    app.debug = True
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True)
