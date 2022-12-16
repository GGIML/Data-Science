# 05-01

## Challenge 04 - Emotions

![](https://www.lepoint.fr/images/2017/06/21/9118894lpw-9119025-article-jpg_4371970.jpg)

## Guidelines

This challenge is more hands-on and less guided than the previous ones.

The folder `src/train` contains a collection of face pictures. This is just a sample of the original dataset that contains more pictures.

The file `src/labels.csv` contains the labels for those images: emotion labels.

The goal of the challenge is to perform a **classification** on this train dataset.

Before doing that, since images are quite big (meaning they have a lot of features), you will have to perform PCA in order to reduce the dimension of your dataset.

Perform a PCA and train a classification model, try to reach the best accuracy on a randomly created test set.