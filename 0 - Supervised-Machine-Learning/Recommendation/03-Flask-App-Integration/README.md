# 04-12

## Challenge 01 - Netflix App 🍿

---
![](https://i.ytimg.com/vi/XxP7epPhhM4/maxresdefault.jpg)
---

## Instructions

Today, we will deploy the movie recommendation engine we have been working on previously! To do so, we will use Flask framework (a Python library for web development), and "serve" our model to anyone!

The server we will use will be in local for now, but as soon as you are happy with your work, you can deploy it on the web and make it accessible to anyone (as a webapp for example).

First, start by installing Flask library:
```python
pip install flask
```

And make sure you can launch the server on your machine. From `netflixApp` folder, run:
```python
python main.py
```

And open `localhost:5000` in your favorite brower, you should successfully see the web app.

We built the skeleton of the app for you 😉 But you need to implement the recommendation part! This is the continuation of what you have been doing in the previous challenge.

1. Start by exploring the `netflixApp` folder. What directories and files does it contain. First, make sure to understand how the app is articulated and what are the different functions of the files.

2. In `utils/` folder, we wrote for you the functions used for loading the files in `load.py`. However, in `reco.py` you need to implement the functions `sims_to_recos`, `get_reco`. It should be quite similar to the ones you created yesterday.

  Read the comments associated to those functions and implement them. Test them (for example in previous notebooks, or in a new one, or in Flask by printing some logs).

3. In `server.py`, use the function created above for populating the variable `recos` containing the recommendations sent to the user.

4. In `templates/recommendations.html`, display the movies recommended to the user (recos computed in Flask backend) as `h4` text to the user.

5. [BONUS] - Display also the movie name and the score associated with that movie in the webapp.

6. [BONUS] - Enrich your results by fetching a movie API to collect info about the movie and/or associated image.
