# 04-03

## Challenge 03 - Implementing Linear Regression from scratch 🥣

---

![](https://media.licdn.com/media-proxy/ext?w=800&h=800&hash=cd%2BdLzyO4UdzzRut2uHerxs1XLs%3D&ora=1%2CaFBCTXdkRmpGL2lvQUFBPQ%2CxAVta5g-0R6nlh8Tw1It6a2FowGz60oISIfYC2G8G2f1spyfNT-tdoDSeLKhpEtOdSsEkBJkcrG-GGGiSp7nWtiIGslz-ZWBZNO1fh4cPzlj1m5ZtN8NNzIDutH1Ia3_ci8Tg6kKTi6bEZrdX1Y0OCgn2sDbIZHpHHsz6WfJH_v5OPpRX-5H4tFv6BNeoJXxA_9v3tQ9hV177gztpej-EQoD7qaKPHDmNXE3H3SVEMZr7KWU1yK_ulXKn1nCoIijLqC7Iq8FyW2Ey_rQUzONgV89r2o71wtOg-RHVCHEjcI2x2-7B8wnZzGC6_a1eHCB7rQh7iIXr87TNDCpbmokmik5V5qFlkwZOtbBlDnJpG5bWu1PK29nid67cfa9z0CgY2BpQnKeRCJ7g-zrlPWhPuU_SNYxkMJBU8oYbQUCedQ_JxuyjsUWGCF-jvxUdAHUexe0z4j8GZl2Yr5UAllVUMLJafNzgb546l-VtR9RedMdV6t6-yI1afYauJidq8yp9PRQkRpmbm734uqxSRbrrenjtA)

Photo by [Tom Crew](https://unsplash.com/@tomcrewceramics)

## Instructions

Remember how we implemented k-NN algorithm from scratch a few days ago?

In this challenge, the goal is quite similar: implement the **Linear Regression model from scratch**.

And when we say from scratch, this time it is really from scratch 😉

OK.., two small hints:
- You should again, implement a **class** with the proper methods **__init__**, **fit**, **predict**
- You can recode the gradient descent from scratch also... but maybe you will prefer to use the function `linalg.lstsq` from `scipy` library 😏
- In this same class, create a function `score` computing the **sum of residual squares** for your predictions. In practice, we prefer to compute the **[R-Squared](https://en.wikipedia.org/wiki/Coefficient_of_determination)** metric (to be discovered soon).

1. Implement the Linear Regression class with proper methods

2. Once you are done, test your new class on `diabetes` dataset from `scikit-learn` library.

3. Plot the data points (therefore, use only one feature for visualization purposes) and draw the linear regression on a 2D chart.

4. Compare your results with the LinearRegression from scikit-learn.

Good luck padawan 🧙‍
