# 04-11

## Challenge 01 - Recommendation - Data Preparation 🎬


![](https://cdn-images-1.medium.com/max/1200/0*ePGWILY6GyplT-nn)

---

## Objectives

You will build a powerful movie recommender 🎬 and deploy it in a Flask application.

## Instructions

This algorithm will work like this:
- You (or any user) selects a few movies he/she likes
- The model returns a list of N movies recommendations corresponding to user's tastes

This project has three steps :
1. First you will **prepare the data** so that we can successfully train a LightFM model [Jupyter Notebook]
2. Then you will **train the model**, and **test your recommendations** [Jupyter Notebook]
3. Finally you will deploy your model into a small web-app, to present your recommendations in a more ergonomic way [Flask webapp]

Good luck in this new project! Open first notebook and follow instructions 🤓

## LightFM installation

We will use the open-source library [LightFM](https://github.com/lyst/lightfm) which provides easy python implementation of **hybrid** recommendation engines.

There are many other libraries in Python for building recommendation engines (ex: Crab, Surprise, etc.). We choose LightFM because it is easy to implement and very powerful (especially if you build hydrid engines).

> As an example, LightFM was largely used by researchers in [RecSys 2018 Spotify challenge](https://recsys-challenge.spotify.com/) (challenge held by Spotify during one of the most popular conference in the field of recommender systems).

⚙️ You can install `LightFM` through `pip`:
```
pip install lightfm
```

⚠️ Some Ubuntu users may encounter problems during the installation process (*>> Failed building wheel for lightfm*, *>> Unable to execute 'gcc'*). In this case, you need first to install gcc compiler :
```
sudo apt-get update
sudo apt-get install gcc
```