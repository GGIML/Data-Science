## Challenge - Iris Species Web App 🌺

![](https://unsplash.com/photos/y4xISRK8TUg/download?ixid=MnwxMjA3fDB8MXxzZWFyY2h8NHx8aXJpc3xlbnwwfHx8fDE2NDk2MzIzMTM&force=true&w=1920)

## Instructions

In this challenge we will create a custom model predicting the species of iris flower based on its measurements and deploy it in **Vertex AI**. We will use the **Vertex AI SDK** to integrate a communication with endpoint and serve it inside a web application made with **Flask**.

⚠️ *for the rest of the challenge please always choose `us-central1 (Iowa)` as your default region*

### I. Cloud Storage

- Upload the [`iris.csv`](https://drive.google.com/drive/folders/11OYMKS1bBJVEXj260aGPk7iOCi4xeji1?usp=sharing) to this newly created bucket.
  
### II. Classification

+ By using pure Python code train a model for the iris species dataset using `Random Forests` and try to optimize the hyperparameters.

### III. Docker Container Creation

- Create a Jupyter Notebook with Scikit-learn, try to choose a standard machine with `1 vCPU, 3.75 GB RAM` . Make sure to use the `us-central1` region.

- From your Jupyter Notebook create a folder named `mpg` ,  which will contain another folder named `trainer` where we will put our training script `train.py`. In this script you must consider reading the dataset from your bucket and saving a dump of the model inside the same bucket in a folder named `model`.

- At the `mpg` folder create `Dockerfile` and consider using an OS image containing Scikit-Learn version 0.23. The `Dockerfile` has to execute the script we've just created.

- Build the image, test it and push the container to the Google Cloud Registry and check if does exist on it.

### IV. Model creation and deployement

+ From **Vertex AI** run the training of this custom model based on what we've seen on the course.

+ Deploy the model to an endpoint

### V. Web App

+ In the webapp folder complete `main.py` to communicate with the model endpoint and get prediction

+ ⚠️ Follow this instructions to authenticate from your machine to the endpoint [Getting started with authentication](https://cloud.google.com/docs/authentication/getting-started)
  
  + Create a service account name `iris-app`
  
  + Choose the role : `Vertex AI Administrator`
  
  + Create a service account key and dowload the json
  
  + Set an environement variable named GOOGLE_APPLICATION_CREDENTIALS and equal to the `KEY_PATH` to the json
