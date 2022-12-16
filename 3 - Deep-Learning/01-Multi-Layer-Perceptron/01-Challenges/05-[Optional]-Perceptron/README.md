# 08-01

## Challenge 02 - Perceptron

---

![](https://www.infomuba.com/wp-content/uploads/sites/328/2019/01/39.jpg)

## Instructions

In order to understand fully what you will be working with later, we will **implement a Perceptron from scratch** 🙂

In this challenge, you will create a **Perceptron** class, with its specific methods and attributes. Let's get started!

This has to be a well documented code: do not forget the docstrings!

### 1. Perceptron Class

1. Implement the `Perceptron` class structure with `__init__` method. The Perceptron class takes 3 inputs: the number of features `n_inputs`, a given list of weights `weights` corresponding to the importance of each input, and a `bias` attribute. Per default you can specify that the Perceptron has for example 3 inputs initialized to a weight of 1 and a bias of 0.

2. Complete your `__init__` method inside the Perceptron class by creating attributes `self.n_inputs` and `self.weights` that represent the attributes of a Perceptron object.

3. Create a first `Perceptron` object called `my_perceptron` and print it. Check the values of the attributes.


### 2. Methods

1. **Weighted Sum**: Write a method `weighted_sum(features)`, that:
- takes as input `features` (of shape  `(n_samples, n_inputs)`)
- returns for a list of `inputs`, the **weighted sum** of the given Perceptron (according to its weights).
2. **Activation Function**: Write a method `activation(sum)`, that returns 1 if `sum` is positive, else 0. This activation function is called the **Step activation function**.
3. Based on the 2 previous methods created, write the method `predict(X)` that returns the prediction (0 or 1) for a given input `X`
4. Test your newly created methods: reuse some of the logic gates examples of the previous challenge, check the results are consistent.

### 3. Training

1. We successfully implemented a Perceptron class! But for now, the weights are fixed by hand. We want to train it, so that it correctly learns how to separate positive labels from negative labels.

  As always in **supervised learning**, we will compare the predicted output (obtained by forwarding the input into the Perceptron, with the `predict()` method) with the target label in order to compute the **error**. In other words:

$$ training error = actual label − predicted label $$

  In a binary classification problem (0 or 1), what would be the different possibilities for the error the perceptron makes?

2. Inside Perceptron class, implement the `compute_error(X, y)` method that compute the errorr obtained for the features `X` and associated labels `y`.

3. Now that you are able to obtain the error made on your predictions, adapt your weights algorithm.

  Create a method `update_weights(error, X)` that updates the `weights` using the Hebb rule. To do that, you have to loop over all the samples in `X`
  
  
4. Finally, implement the `fit(X, y)` method, that computes the error and updates the weights of your perceptron with $\alpha=0.1$, and does that 100 times (this arbitrary number 100 is actually the so called **number of epochs**.

5. Make sure your code works by loading the Breast cancer dataset in scikit-learn and by fitting your Perceptron model to the data. What are the final values for the weights? 
Compare your results with the sklearn implementation of the Perceptron.

### 4. Improvements

Now, let's complete our Perceptron class with some additional attributes:  

1. Create a new attribute `epochs` that allow us to configure the number of epochs during the training
2. Include a `learning_rate` attribute, that specifies the amount of update at each step (the parameter $\alpha$ in the Hebb rule)
3. Add an instance variable `self.activation` that can take several strings: `'sign'`, `'step'`, `'sigmoid'`, `'relu'`, `'tanh'` and try to adapt the fit and predict code accordingly
