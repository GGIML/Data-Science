# 07-04

## Challenge 03 - Further with Spark DataFrames
---
![](https://images.unsplash.com/photo-1511713724866-102ba72ac216?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)
Picture by [Maxi am Brunnen](https://unsplash.com/photos/FOyhzt-ryM0)

## Instructions

#### Workspace setup

**Q1)** Load the Spark Session and name it as you like.

**Q2)** Download the Paris trees dataset in CSV format.

[Source : Paris Open Data](https://opendata.paris.fr/explore/dataset/les-arbres/information/)

**Q3)** Create a DataFrame from the CSV file.

Syntax is ```df = SparkSession.read.csv("FILENAME", header=boolean... )```

**Q4)** Explore your dataframe :

You can use functions like **show**, **select**, **dtypes**, **describe**, **filter**, **count**.

Here as some cells with suggested manipulations. Here it is important to understand how to chain instructions on a dataframe.

**Q5)** Deleting a column

We have seen in the previous question that we can chain multiple operations on a dataframe. BUT, all we did in the previous cells did not modify our dataframe.

If you want to modify a dataframe, you have to reassign the variable.

Obviously, we will not use the ```geo_point_2d```. Reassign the dataframe (df), or create a new variable, and drop the column.

##### In the following questions I want you to discover the .withColumn() operator. It's one of the most useful tool for manipulating columns.

**Q6)** Renaming a column :

We'll start with the **.withColumnRenamed** operator, to rename a column. Change the "LIEU / ADRESSE" to "ADRESSE".

Syntax : ```df.withColumnRenamed("colName", "newColName")```

Dont forget you have to reassign a variable for your instruction to be applied.

**Q7)** Modify a column :

.withColumn applies an operation to a whole column. It creates a new column with the name given. If you give the same name, the column will be replaced.

Apply the withColumn function to concatenate the columns NUMERO and ADRESSE, into a new column named ADRESSE_COMPLETE.

#### SQL queries to dataframe
