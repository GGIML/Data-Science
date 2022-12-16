# 07-04

## Challenge 01 - Spark Installation

---
![](https://images.unsplash.com/photo-1508610232556-b13ab6d792b2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1276&q=80)
Picture by [Jamie Street](https://unsplash.com/photos/qSGqR5WvOnU)

## I. Download and install Spark

### [UBUNTU] - Download & Install

👉🏻 [Medium article : installing Spark for Ubuntu](https://medium.com/@GalarnykMichael/install-spark-on-ubuntu-pyspark-231c45677de0)

1. Prerequisites
	- Have Java installed : * Check with `java -version` in your terminal
		* If not installed run `sudo apt-get update`
		* Then `sudo apt-get install default-jdk`
	- Have python installed

1. Download the latest Spark version [here](https://spark.apache.org/downloads.html)

1. Uncompress the file in your working directory with `tar xvf spark-2.X.X-bin-hadoop2.7.tgz` (not in your git repo please, somewhere like /home/name/programs/)

1. Add the following lines in your ~/.bashrc (or ~/.zshrc) file
```bash
export SPARK_HOME=__CompleteSparkFolderPath__
export PATH=$SPARK_HOME/bin:$PATH
```
where `__CompleteSparkFolderPath__` is for example : `/home/username/programs/spark-2.4.3-hadoop2.7`

At this point, you have a spark folder in your working directory: that's all for installing Spark. This directory contains everything spark needs.

### [MAC OS] - Download & Install

👉🏻 [A (too) complete guide for Spark install on macOS](https://medium.com/luckspark/installing-spark-2-3-0-on-macos-high-sierra-276a127b8b85)

🔦Hint : First, download Spark, and see what is missing before installing anything else (Java, Scala, Python) because you may already have everything.

1. If needed, have java & python3 installed. [Here](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) for install Java-JDK8.

1. Download the latest Spark version [here](https://spark.apache.org/downloads.html)

1. Extract it somewhere, **not your git folder**, somewhere like `home/username/programs`

1. Add the following lines in your ~/.bashrc (or ~/.zshrc) file
```bash
export SPARK_HOME=__CompleteSparkFolderPath__
export PATH=$SPARK_HOME/bin:$PATH
```
where `__CompleteSparkFolderPath__` is for example : `/home/username/programs/spark-2.4.3-hadoop2.7`

➡️ At this point, you have a spark folder in your working directory: that's all for installing Spark. This directory contains everything Spark needs. You may restart your terminal before doing the following steps.

## II. Running Spark with `spark-shell`and `pyspark`

1. All the Spark executables are located in the **bin** folder. Try ```spark-shell``` command in your terminal. You should see the Spark logo, followed by a Scala prompt. This is normal, scala is the core language of Spark.

2. In the new Scala prompt, try executing a scala command : ```println("Spark is running")```. Don't quit the `spark-shell` yet.

3. Now, have a look in your terminal, Spark has prompted some informations above the Spark logo. **Have a look at the WebUI address given**. This is where you can monitor what is happenning under the hood, find logs of your jobs, find DAGs... We will come back to this in the next challenge. You can then exit the spark shell using Ctrl-C.

4. Similarly, you can run a PySpark shell. Try launching `pyspark`. You should see Spark logo, and Python prompt. Try some python commands like defining a list of strings. Does it work ? You can quit PySpark prompt with ```exit()```.


## III. Running Spark in Jupyter Notebook

👉🏻 [Getting started with Pyspark jupyter](https://blog.sicara.com/get-started-pyspark-jupyter-guide-tutorial-ae2fe84f594f)

1. Configure PySpark driver so that running `pyspark` will **automatically** open a Jupyter Notebook. Add the following lines in your ~/.bashrc (or ~/.zshrc) file :
```
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
```
1. You can also load a regular Jupyter Notebook with `jupyter notebook` and then load **manually** PySpark using findSpark package. You shoul  first `pip install findspark`. Then, in the first cell of your notebook :
```python
import findspark
findspark.init('home/username/folder/spark-2.4.3-hadoop2.7')
from pyspark.sql import SparkSession
```
