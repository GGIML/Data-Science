# 07-04

## Challenge 02 - Launching Spark, Dataframe discovery
---
![](https://images.unsplash.com/photo-1430116267665-e7f6b3dafce3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)
Picture by [Wil Stewart](https://unsplash.com/photos/2aCuwSh4RRk)

## Instructions

You will find everything you need in the notebook in `src` folder.

1. Launch a SparkSession

2. Retrieve the Spark Web UI adress, open it in a new tab and keep it for later

3. Create a Dataframe from the [Uber CSV file](https://drive.google.com/open?id=1hLjLVuryuWd7OmeJ5rXp2YJ0BEIFyLaS), you will pass 3 parameters :
    - The file name
    - A boolean parameter : header
    - A boolean parameter : inferSchema

4. Check the python type of your Dataframe, do you recognize the Spark library used here ?

At this point, we already have done a lot, with not so many line of codes.

**Let's have a closer look at our Dataframe. Just like Pandas Dataframes, you can call simple function to gain insights.**

5. Have a look at the first lines of your Dataframe. *Hint : "Show me the lines"*

6. Find the function for retrieving the **Schema** of your Dataframe. *Hint : "Print the Schema"*

7. Display the line count of your Dataframe. You should have 1474 lines.

8. Apply a function to describe your Dataframe. *Hint : Very similar to Pandas describe, just add a .show() at the end.*

9. Apply the describe function on two integer columns. *Hint : Use a .select()*

**Now that you have played around with your dataframe, you can go back to your WebUI.**

10. Navigate the jobs, and find the DAG of a job *Hint : it's 2 clics*
