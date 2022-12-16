# 06-04

## Challenge 01 - Quora Insincere Questions Classification

![logo](images/quora.jpg)


## Objectives

Quora is a popular website where anyone can ask and/or answer a question. There are more than 100 millions unique visitors per month.

Like any other forum, Quora is facing a problem: toxic questions and comments.

As you can imagine, Quora teams cannot check all of the Q&A by hand. So they decided to ask the data science community to help them to perform automatically insincere questions classification.

## Guidelines

This challenge was launched on Kaggle : https://www.kaggle.com/c/quora-insincere-questions-classification

Read the overall information on Kaggle. Quora provided a dataset of questions with a label, and the features are the following:

- `qid`: a unique identifier for each question, an hexadecimal number
- `question_text`: the text of the question
- `target`: either 1 (for insincere question) or 0

📥 The Kaggle dataset is quite heavy and it may be too difficult for your laptops to perform the computations. Therefore, we provide you with **the train dataset** (to be sampled) and also **light word embeddings**, which you can download [here](https://drive.google.com/open?id=1JW4TvRn7BLCV8W2YIHXCaajBMJICJwJ-).

⚠️ Don't look at the published kernels, in order to keep your judgement unbiased.

👉🏻 Here are a few steps to follow :
1. First sample the dataset to 10.000 lines otherwise your laptop might die ☠️ (you may need to use `sklearn.utils.resample()`)
1. As usual, begin with a proper EDA
1. Perfom a nice text preprocessing
1. Try to run a quick sentiment analysis your classical machine learning models.
1. Then, use a word embedding (Glove) to create your corpus and run your model.
1. Do some optimization (text preprocessing, model hyperparameters, other word embeddings if you trust your computer 💻)
1. Optimize ++: Now, let's have a look at some published kernels and find some inspiration.
1. 🎁 Bonus question : try to identify the most recurrent topics in toxic questions !

🔦 In this competition, the metric used for performance evaluation is the **F-score**.