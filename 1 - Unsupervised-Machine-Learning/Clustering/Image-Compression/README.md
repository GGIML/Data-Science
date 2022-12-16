# 05-02

## Challenge 05 - Image Compression

![](https://lisaspringercom.files.wordpress.com/2019/01/neil-thomas-736941-unsplash.jpg?w=1140)

## Guidelines

In this challenge, you have to perform an image compression of the given picture of New York (`NewYork.jpg`). To do so, we want to keep not all the possible colors, but only 4. Thus, you have to perform a k-means algorithm, with k=4, and show the image with those only 4 colors.

> 🔦 **Hint:**: An image is composed of pixels. Each pixel is made of 3 channels: Red, Green, Blue (RGB). Those color levels are encoded on 8 bits, meaning they are in the range [0-255]. For example, a pixel with this RGB color : (0, 0, 255) will be a very strong blue pixel.
