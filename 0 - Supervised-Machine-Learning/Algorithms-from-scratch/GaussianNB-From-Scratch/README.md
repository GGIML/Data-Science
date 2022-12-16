# Challenge - Recoding a GaussianNB from scratch

![](https://images.unsplash.com/photo-1530639834082-05bafb67fbbe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80)

## Objectives

In this challenge, you will recode the Gaussian Naive Bayes algorithm **from scratch**. <br>
This is not an easy exercise, but coding ML algorithms yourself is the best way of making sure you have a good understanding of them :)

## Guidelines

A quick reminder on **Naive Bayes classification** :
1. The NB classifier is based on the **Bayes Theorem** :

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1Szw5qZYBoOxv6Wn7CSZbiBFcLpqxSvIy" style="width:400px">
</p>

In the above formula :
- $Pr(Y=y_k|X=x)$ is **the probability of each class given the known features**
- $Pr(X=x|Y=y_k)$ is **the probability of the features given the class**
- $Pr(Y=y_k)$ is **the probability of apparition of the class on the given dataset**
- $Pr(X=x)$ **does not actually need to be computed**

Using the Bayes formula, **the algorithm computes the probability of each class for a given set of features, and returns the class with the higest computed probability**.

2. $Pr(Y=y_k)$, the probability of apparition of the class on the given dataset, is very easy to compute : it is just **the percentage of apparition on each class on the training set**.

3. $Pr(X=x|Y=y_k)$, the probability of the features given the class, is a little bit harder to compute, but no stress, let's go step by step :
- The probability of all features given the class is equal to the product of **the probability of each single feature given the class**.
- And **the probability of each single feature given the class can be computed using the following (gaussian) formula** :

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1_QVFGAB0JhriodMVxv4io_d-Rkd3wO6j" style="width:400px">
</p>

In the above formula :
- $\mu_k$ is the mean of the feature $x$ for a given class $y_k$
- $\sigma_k$ is the standard deviation of the feature $x$ for a given class $y_k$

⚠️ **The values of $\mu$, $\sigma$, and the probability of apparition on each class over the training dataset is what the algorithm learns during the fitting stage.**