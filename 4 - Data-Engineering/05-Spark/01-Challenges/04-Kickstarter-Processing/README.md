# 07-04

## Challenge 04 - Kickstarter preprocessing
---
![](https://images.unsplash.com/photo-1530083727892-3c261661d7a4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)
Picture by [Steve Halama](https://unsplash.com/photos/GjSzvtZhMoA)

## Instructions

In this exercise, we will start working on the Kickstarter dataset, each record is about a specific campaign. Today, you will pre-process the dataset. During the next Spark course, you will apply machine learning to it.

**Q1)** Have a look at our train_clean.csv file, with the linux ```head``` command.

**Q2)** Create the spark session variable, name it "preprocessing".

### Loading & exploring data

**Q3)** Load the data from the train_clean.csv. We have seen at Q1 that this file has a header.

**Q4)** Let's go for some exploration :
	- 4.1) Number of lines and columns.
	- 4.2) Display the first 20  rows of the dataframe.
	- 4.3) Print the schema of the dataframe.

**Q5)** When printing the schema, we see that all columns are strings. Assign the integer type to columns you think appropriate. Have a look at the csv file. This new dataframe will be named dfCasted, print its schema.

*Hint : Use the .withColumn(newColName, newColValue) to cast each column.*

**Q6)** We could have done this much faster. Do you know how ?


### Data Cleaning

**Q7)** Give a statistical description of these columns together : goal, backers_count, final_status

**Q8)** Let's have a look at the **disable_communication** column. Group by values and display a descending value count. Show the top 10 values.

*Hint : groupBy, count, orderBy, show*

What do you notice ? Considering the number of lines of our dataset, does this column provides information ?

**Q9)** Houston, we have a problem ! We can see the future in our dataset ! Can you find it ? These informations must be removed.

*Hint : There are two problematic columns, it has something to do with the supporters, and a change during the project.*



**Q10)** Country & Currency : Start with some exploration of these columns.

- Try some groupBy and counting, just like *Q8*. Then, read below.

You may think that *country* and *currency* are redundant, in which case we could just delete one of the two columns. What about Euro ?

- Try selecting *goal* and *final_status*, and show some values.

- Try showing value count for country and currency in the same table.

**Q11)** Now, there is something else : Some values for *country* have the value *False*. Display these records, and groupBy *currency*, descending.

*Hint : The instruction chain is the following : dfCasted.filter().groupBy().count().orderBy().show(), fill 3 parentheses.*

*Definition - Custom functions :* Some column operations are already defined inside Spark, but we often need to apply more complex or more custom function. In this case, we can create User Defined Functions (UDF) and apply them on columns.

**Q12)** In this question, we will create two UDF.
- **udfCountry(country, currency)** : If country=False, take the currency value, else, leave the country value.
- **udfCurrency(currency)** : If the length of currency is different than 3, assign a null value, else, leave the currency value.

**Q13)** In this question we will apply our two UDF. Using the .withColumn operation, you can change a column, just like you did for type casting. withColumn will create two new columns : country2 and currency2.

*Hint : df.withcolumn(country2, newColValue).withcolumn(currency2, newColValue)*

Also, you can add a drop statement (on country and currency) after the two withColumns, as we have created our new columns.

Check your dataframe once transformations are applied. Schema and first lines.

**Q14)** We will do one more cleanup on the column **final_status**, which will be the label for our classification algorithm in next course.

First, count the number of elements for each values in final_status.

Finally, we need to delete records with **final_status** different than 0 or 1.


### Feature engineering

It's sometimes useful to add features to our dataframe, to help our model learning. We will work with the time data.

**Q15)** Our dates columns are in unix timestamps. We first need to convert them to dates.

**Q16)**
Add a **days_campaign** column, which represents the duration of the campaign, in days. This is the difference between *launched_at* and *deadline*. Here we work with a date difference.

Add a **hours_prep**, which represents the number of hours of preparation. This is the difference between *created_at* and *launched_at*. You may round to 2 digits after comma. Here we work with a timestamp difference.

Finally, apply a filter : we want to delete records with **days_campaign** AND **hours_prep** equal to zero, and we want the records with **goal** greater than zero

**Q17)** At this point, we don't need these columns anymore : *created_at*, *launched_at*, *deadline*.

We will now work on text data, we will gather every text values into one.

**Q18)** Pass the columns *name*, *desc* and *keywords* into lowercase.

**Q19)** Create a new column called *text* which contains the three previous columns. Be careful to include a space between them so that we can split them later.

**Q20)** You can now delete these three text columns.


### Processing null values

**Q21)** There are various techniques to handle null values to make them usable by an algorithm. Can you find 3 different methods ?

**Q22)** For the columns *days_campaign*, *hours_prep* and *goal* : replace null values by **-1**.

**Q23)** For the columns *country2* and *currency2* : replace null values by **unknown**.


### Exporting Dataframe

Well done, you have done a pretty good pipeline for pre-processing your dataset.

**Q24)** Finally, export your dataframe to the *parquet* format.

*parquet* always exports a folder that may contain multiple files, this is due to the distributed nature of Spark.
