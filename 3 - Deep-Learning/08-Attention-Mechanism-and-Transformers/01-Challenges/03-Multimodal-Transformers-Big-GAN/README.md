# Challenge - Multimodal Transformers Big-GAN

![](https://images.unsplash.com/photo-1512572525676-f9b59951929e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=952&q=80)

This is a multimodal exercise. The main idea of the challenge is to unify Natural Language Processing models
and Generative Adversarial Networks (GAN) to generate random images from text.

## Generative Adversarial Networks (GAN)

Generative Adversarial Networks, or GANs, are neural network architectures that can generate images.

For this exercise you don't need to fully understand what a GAN is, it will be covered here at Vivadata by the end of the week.
You will only need to understand a few specificities about the Big-GAN, which will be explained below.

### BigGAN

The BigGAN is trained on ImageNet to generate an image from a set of inputs consisting of:

- a noise vector (of length 128 for BigGAN), typically randomly initialized for each sample from a truncated normal distribution, and
- a one-hot class vector (of length 1000) indicating which of the 1000 classes of ImageNet the image should be generated for, where each index correspond to a class (for example: 154 for dog, 281 for cat or 1 for fish)

The first step of BigGAN's forward pass is to convert the one-hot 1000-dim class vector in a dense class vector (of length 128) representing the associated ImageNet class using an embedding projection matrix similar to a typical word embedding matrix.

The noise vector and the dense class embedding are then concatenated in a single input vector of length 256 which is used for the image generation process.

For this exercise, we will be only interested in the embedding of each class.

## Generating image from text using Transformers and Big-GAN

In this exercise we want to see if a good language understanding model (like BERT) can be combined with a good image generation model (like BigGAN) to **generate good quality images from text** end-to-end in a creative proof-of-concept application.

Here is the target workflow:

- the user inputs some text, e.g. "I have a cat",
- a pretrained language model (e.g. DistilBERT) converts the text in contextualized hidden-states embeddings
- a mapping model (that you will build in the exercise) converts the contextualized hidden-states embeddings in a input vector for a pretrained image generation model (BigGAN)
- the pretrained image generation model converts the input vector in an image, hopefully the image of a cat.

Here is an illustration of what we are trying to build:

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1RN93Q_MaiS5UQBvQYWH3ixAYL3OyMVvR">
</p>

## Some words on aligning latent spaces

As we can see we basically have two latent spaces that were trained separately:

- Transformers embeddings, which, in the case of BERT, are in a 768-dimensions latent space and are associated to text tokens
- BigGAN embeddings which are in a 128-dimensions latent space and are associated to each ImageNet class (the noise vectors don't really have usable information content).

We would like to build a mapping between these two embedding spaces to connect the two models in a relevant way so that a text input like "I have a cat" would generate the image of a cat.

Learning a mapping between two independently learned latent spaces has been investigated in fields like unsupervised machine translation. A logical solution, first proposed by [Mikilov et al. in 2013](https://arxiv.org/abs/1309.4168), involves learning a mapping between both embedding spaces learned from a set of seed points mapping one space to the other.

We'll use the ImageNet classes as a database to generate seed mapping points between our two models. In our case we can see that:

- on the one hand, each ImageNet class can be associated to one (or several) text label(s) like "cat", "dog", "car" and so on,
- on the other hand, our pretrained langage model can generate hidden-states from provided sentences containing these words, for instance "I have a cat", "My dog is barking" or "This car was driving fast".

From these two associated sets of text inputs we can thus:

- manually create a dictionnary of text sentences associated to each ImageNet class,
- extract embeddings associated to both, by computing BERT's output as inputs `Xi` for our mapping function and extracting the relevant ImageNet dense class vector `Zi` from BigGAN's input embedding matrix as target.
- use this seed dictionnary of associated `Xi` and `Zi` to learn a mapping function from the language model hidden-states to relevant input vectors for BigGAN.

Obviously, the generalization of such a procedure on random text outside of the fine-tuning distribution of seed sentence, or outside of the ImageNet training classes, will not be garanted and the multi-model systems will probably generate more unpredictable images.
