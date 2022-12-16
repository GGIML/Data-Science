# 04-07

## Challenge 01 - Flag Scanner 🇧🇯🇨🇳🇧🇧🇪🇨🇨🇺🇬🇦🇫🇮

---

![](https://www.probuilder.com/sites/probuilder/files/styles/con/public/oleh-aleinyk-711501-unsplash.jpg?itok=2wp-5ulq)

## Instructions

In this exercise, we will train a **Decision Tree** model that predicts the continent of a country based on its flag.

The data comes from this open dataset: http://archive.ics.uci.edu/ml/datasets/Flags

You will make sure to create **reproducible results** by stating a `random_state` anytime it is required.

Follow the steps below:

1. Load the dataset in a DataFrame variable named `flags`. Make sure to include row 0 as header as it contains the column names.

  What is the shape of the data, what features (and how many) does the dataset contain?

2. Create a DataFrame variable `y` corresponding to our target variable column.

3. Create a DataFrame variable `X` containing only the following features columns:
  - "Red"
  - "Green"
  - "Blue"
  - "Gold"
  - "White"
  - "Black"
  - "Orange"


4. Split your data into a training set of 70% and a testing set with the remaining lines.

5. Fit a **`DecisionTree`** classifier on your data and **evaluate your model**. What would be the score of *random guessing* the continent? Compare with your model performance.

6. We have a first performance benchmark. Using `GridSearchCV`, train your tree with `max_depth` value varying from 1 to 20 and observe the impact on your accuracy.

  Plot these results in a chart with x-axis for depth of the tree and the y-axis corresponding the tree's accuracy.

7. > 🔦 **Hint**: Our graph does not really look like what we expected. The depth of the tree does not have a clear impact on the tree score. This might be a good indication that we are not using enough features.

  Add all the features associated to the the shapes of the flag, and redo the analysis. What does your graph look like after making this change?

8. Explore on your own and try improving the score of your decision tree. Here are some suggestions on improvements:
  - Tune other hyper-parameters. Think about whether you are overfitting or underfitting the data based on the hyper-parameter selected and the value chosen
  - Select a subset of features that work better on this data  
