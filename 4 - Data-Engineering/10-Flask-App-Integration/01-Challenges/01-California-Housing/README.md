## Challenge - California Housing 🏘️


![](https://images.unsplash.com/photo-1519227355453-8f982e425321?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1489&q=80)


## Instructions

You'll be creating a small web application using Flask. The objective is to predict the median housing value of a Californian district based on a pre-trained model.

The folder `california_housing_webapp` contains the canvas you'll be using. All your code must be inside `main.py`.

First, start by installing Flask library:

```python
pip install flask
```

Now here are your tasks.

1. Use the California Housing dataset and train a model on it.

2. Save this model into a pickle file.

3. Your main page at root (meaning URL `/`) has to display the page containing the data to fill. In other words you have to render in your root (`/`) the HTML file `index.html`.

4. Create a function supporting the `POST` method, where you will gather the data from the previous form and predict the median housing value and display it by putting in a variable named `price` and render `prediction.html`.

5. Repeat the task N°4, but this time using FastAPI. Instead having the prediction business logic inside of Flask, use it just as a "display" application and call the proper API interface to do your prediction. (hint: you'll use `requests` to communicate with the API).

```python
import requests
r = requests.post('http://127.0.0.1/predict/', json={"key": "value"})
prediction_response = r.json()
```

⚠️ If you are using Windows, you will need to run the following commands in your terminal (when located in the folder containing the `main.py` file) to launch your Flask app :

```bash
export FLASK_APP="main"
flask run
```
