# Challenge - MapReduce in Java

---

![](https://images.unsplash.com/32/6Icr9fARMmTjTHqTzK8z_DSC_0123.jpg?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1052&q=80)

## Instructions

WordCount is one of the most basic jobs you can think of for MapReduce. In this exercise, we'll use a pre-compiled Java code and create a new job on Hadoop to count the occurence of words in a book.


# I. WordCount

In this exercise, we will perform a simple WordCount : from an input text, we will count how many times each word appears, and rank the final list by occurence. MapReduce is of course not needed for such task, and a simple Python script on your computer would be fine. But what if your input text is a whole book ? Thousands of books ? Millions of books ? ...

### Pre-requisite

Hadoop runs only on GNU/Linux platforms. Therefore, if you have another OS, you need to install **Virtual Box**. Virtual Box is a software that lets you create and run Virtual Machines. 

**A virtual machine** is a machine that takes part of the resources of your computer (according to initial parameters you chose), and for which you can choose the OS to boot on within the software.

## Step 1 : Install Virtual Box

The first step of this exercise is to install Virtual Box if you don't have a Linux operating system.

1) Go to : https://www.virtualbox.org/ and download VirtualBox.

2) Follow the installation steps.

## Optional : Launch Ubuntu VM (30mn)

This part is optional, and is simply here for you to understand how to install a complete Ubuntu VM on your computer.

Go to [this link](https://www.ubuntu.com/download/desktop) and download the Ubuntu Desktop file.

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1UFDkGZIymkB7dDC5flyseK6G2h0WSbP3">
</p>

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1bgCskCx5qxbnm-3_YZ_1hPYg63qeUvit">
</p>

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1PNAYb00YiwBbFzrqkVle5mhLXPNSG17h">
</p>

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1AYk3r0PcECz7hKX8XbSsOaKBnDpnH8VI">
</p>

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=13MO-HdDuw0aivhCQDTOIwz1Y76qi70e1">
</p>

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1Eki_iWqU33MYB6yT37KAaYMFQf5qR3va">
</p>

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1K3z0iAuSPvUatonlaZmNUFKSZOM1CNeH">
</p>

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1HIvSDG4fC8c9Zrro3nh1BJ23dlH5wknL">
</p>

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=18JGXOH3ykLvE3zgqbBmdCTmcUY89PhDF">
</p>

Here's what you should see :

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1IYwp1XbpuxYw7fNwuSDw0IQV7lvXe7We">
</p>

Click on "Install Ubuntu", set your keyboard, and choose Minimal installation :

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=152lOBGnx58VxD1m_nQCsexI7Ofiuzab8">
</p>

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1Biokv48mDrR4LN0tLBW1hNnCwQu1QnMA">
</p>

Follow the steps until you have to restart the VM. You might need to quit the installation and restard the VM from the menu. You should finally see you user interface :

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1EVlXtiqrwPs0QWQ9VDCUfARHwcFhsMcN">
</p>

## Step 2 : Hortonworks  Sandbox and MapReduce

### 1. Getting started with the VM

**a) Install and launch**

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1WmV_cbvBLRFEFhKKTtHkkGYhUjkpUq3X">
</p>

The Sandbox by Hortonworks is a straightforward, pre-configured, learning environment that contains the latest developments from Apache Hadoop, specifically the Hortonworks Data Platform (HDP). The Sandbox comes packaged in a virtual environment that can run in the cloud or on your personal machine. Sandbox also offers a data-in-motion framework for IoT solutions called Hortonworks Data Flow (HDF). To configure Hadoop from scratch on a Linux VM, this tutorial might be useful : https://www.tutorialspoint.com/hadoop/hadoop_enviornment_setup.htm


Hortonworks offers a way to use Hadoop Tools connecting to a Virtual Machine in SSH for command lines interfaces. Numerous web interfaces are also available. 

The sandbox can be downloaded from here : 

https://www.cloudera.com/downloads/hortonworks-sandbox.html

Download the **HDP** Sandbox. This Sandbox makes it easy to get started with Apache Hadoop, Apache Spark, Apache Hive, Apache HBase, Druid and Data Analytics Studio (DAS). Choose the VirtualBox installation type.

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1SgOlN4dZx_8g2O8FbUhdzQJLXeWeBqdL">
</p>

Fill in the form and download the **version 2.6.5** of the Sandbox. The sandbox requires around 15 Go of space.

Once this is done (the download might take a really long time) :
- Open VirtualBox
- Click on "New"
- Go in "Fichier -> Importer un appareil virtuel". 
- Select the image of the Sandbox you just downloaded.
- Start the VM

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1JfMuGF67heCE53JTLU7KkxU3OyPch7M7">
</p>

The first boot takes a while, so time for a break !

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1ou9Si9wRQLfQbYWpq2RldXdG_x5o39YI">
</p>


**b) Access the Sandbox**

The application is now ready to be used :

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1uaSwzwrXbW6WYCRS1dTthS3zp1yD3OL0">
</p>

**User** 

Once started, the Sandbox is accessible from your local computer, in SSH, on the Port 2222. We will be using username : `raj_ops` and password `raj_ops` as it is pre-registered. 

There are many pre-configured users for the HortonWorks Sandbox, including :

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1P7Xi97H5wEUr3-QaAwKeJQIRDoWL3NFD">
</p>

**SSH**
Launch your terminal and access the Sandbox using SSH :

`ssh raj_ops@localhost -p 2222`

If you are asked whether you'd like to permanently add 2222 to the list of known hosts, say Yes.


**Splash Page**

We should be able to access a graphical view of the services available on a Hadoop cluster. It's called the VirtualBox Splash Page, and it can be accessed on :

`http://localhost:8080`

You will be asked to log-in :

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1zUV_Nf_sG95v2tKfPUWB8mjIprTdpbeF">
</p>

Then, after loading, the page should look like this :

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1ROduAIiLT3Jo1lj2LYbWsS7hx6beLKR4">
</p>

Explore the Dashboard and try to understand the main components.

### 2. Getting started with HDFS

**a) Create a repository on the VM to download the data**

Using command lines :

`[raj_ops@sandbox-hdp ~]$ mkdir TP`

`[raj_ops@sandbox-hdp ~]$ cd TP`

**b) Download the data and the JAR file**

Download the .txt file we'll be using for our WordCount from here : https://norvig.com/big.txt

In the TP repository, you can use the command line directly :

`wget https://norvig.com/big.txt`

You should have something like this :

`[raj_ops@sandbox-hdp TP]$ wget https://norvig.com/big.txt`

If everything worked well, by typing `ls`, you should see the file `big.txt`.

You will now also add the Jar file, which contains the Java code to execute a MapReduce :

`wget https://github.com/maelfabien/maelfabien.github.io/blob/master/assets/files/wc.jar`

This code is a pre-compiled version of the code available here : https://hadoop.apache.org/docs/r2.8.0/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html#Example:_WordCount_v1.0

If we try to detail just a little bit the Java code :

```java
import org.apache.hadoop.conf.Configuration ;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat; 
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {
    public static class TokenizerMapper
    extends Mapper<Object , Text , Text , IntWritable>{
    
    private final static IntWritable one = new IntWritable (1) ;
    private Text word = new Text();
    
    public void map( Object key , Text value , Context context ) throws IOException , InterruptedException {
        StringTokenizer itr = new StringTokenizer(value.toString()); 
        while ( i t r . hasMoreTokens () ) {
            word.set(itr.nextToken());
            context.write(word, one);
        } 
    }
}
    
public static class IntSumReducer
extends Reducer<Text , IntWritable , Text , IntWritable> {
    private IntWritable result = new IntWritable () ;
    
    public void reduce(Text key , Iterable<IntWritable> values ,
        Context context) throws IOException , InterruptedException {
    int sum = 0;
    for (IntWritable val : values) {
        sum += val.get();
    }
    result.set(sum) ;
    context.write(key, result);
    } 
}
```

```java
public static void main(String [] args) throws Exception {
    
    #Provide a configuration of the cluster:
    Configuration conf = new Configuration () ;
    
    #Call the constructor with the configuration object and a name for the job
    Job job = Job.getInstance(conf, ”word count”);
    
    #Provide an implementation for the Map Class
    job.setMapperClass(TokenizerMapper.class);
    
    #Provide an implementation for the Combiner Class
    job.setCombinerClass(IntSumReducer.class);
    
    #Provide an implementation for the Reduce Class
    job.setReducerClass(IntSumReducer.class);
    
    #Specify the type of the output key/value
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    
    #Give the location of the input/output of the application
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    
    #Specify how the input/output will be formatted
    job.setInputFormatClass(TextInputFormat.class);
    job.setOutputFormatClass(TextOutputFormat.class);
    
    #Start the job and wait for its completion!
    job.waitForCompletion(true);
}
```

**c) Move file to HDFS**

Hadoop commands launches by default on a working repository based on the name of the user : `/user/<user_name>` 

- We need to create the repository from our SSH connexion : `/user/raj_ops/TP/input`, and upload our file to HDFS.

`hadoop fs -mkdir -p TP/input`

- We have downloaded the datas under the `big.txt` file. We will upload the file on the folder :

`hadoop fs -put big.txt TP/input`

- In this command, `big.txt` is in the local repository on the linux VM whereas the `TP/input` makes reference to a file in HDFS. We can display the last 5 lines of the file `big.txt` located in HDFS :

`hadoop fs -cat TP/input/big.txt | tail -n 5`

The book ends on a function written in Python 2, so you should see something like this :

`if ord(c) > 127 and c not in s:`

`print i, c, ord(c), big[max(0, i-10):min(N, i+10)]`

`s.add(c)`

`print s`

`print [ord(c) for c in s]``


**d) Additional commands**

To add files, insead of using `hadoop fs -put filename`, we can simply drop them and create folders through the file System offered by Sandbox. 

To delete a file, move to Trash or use `hadoop fs -rm filename`. However, it does not properly speaking delete the file, but moves it to the trash. You need to purge the trash frequently :

`hadoop fs –expunge`

`raj_ops` does not have the rights to purge the trash.

### 3. Launch a MapReduce Job

There are several commands we can use over `hadoop`:

- `namenode -format` : Formats the DFS filesystem.
- `secondarynamenode` : Runs the DFS secondary namenode.
- `namenode` : Runs the DFS namenode.
- `datanode` : Runs a DFS datanode.
- `dfsadmin` : Runs a DFS admin client.
- `mradmin` : Runs a Map-Reduce admin client.
- `fsck` : Runs a DFS filesystem checking utility.
- `fs` : Runs a generic filesystem user client.
- `balancer` : Runs a cluster balancing utility.
- `oiv` : Applies the offline fsimage viewer to an fsimage.
- `fetchdt` : Fetches a delegation token from the NameNode.
- `jobtracker` : Runs the MapReduce job Tracker node.
- `pipes` : Runs a Pipes job.
- `tasktracker` : Runs a MapReduce task Tracker node.
- `historyserver` : Runs job history servers as a standalone daemon.
- `job` : Manipulates the MapReduce jobs.
- `queue` : Gets information regarding JobQueues.
- `version` : Prints the version.
- `jar <jar>` : Runs a jar file.
- `distcp <srcurl> <desturl>` : Copies file or directories recursively.
- `distcp2 <srcurl> <desturl>` : DistCp version 2.
- `archive -archiveName NAME -p <parent path> <src>* <dest>` : Creates a hadoop archive.
- `classpath` : Prints the class path needed to get the Hadoop jar and the required libraries.
- `daemonlog` : Get/Set the log level for each daemon

To launch the Hadoop MapReduce job, you should simply type the following command :
    
`hadoop jar wc.jar WordCount TP/input TP/output`


You can see the cluster work from this page : http://localhost:8088/

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1V9FUhp0KzJtYfNQRzFUtQ1GejGre8ZjK">
</p>

### 4. YARN

This page displays the work done on YARN. Apache Hadoop YARN is the resource management and job scheduling technology in the open source Hadoop distributed processing framework. One of Apache Hadoop's core components, YARN is responsible for allocating system resources to the various applications running in a Hadoop cluster and scheduling tasks to be executed on different cluster nodes.

YARN stands for Yet Another Resource Negotiator, but it's commonly referred to by the acronym alone.

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1QPVJ2wjPZ6DqgYZVEOa3WZmWfJdff3k4">
</p>

Apache Hadoop YARN decentralizes execution and monitoring of processing jobs by separating the various responsibilities into these components:
- A global **ResourceManager** that accepts job submissions from users, schedules the jobs and allocates resources (CPU, RAM, Disk) to them.
- A **NodeManager** slave that's installed at each node and functions as a monitoring and reporting agent of the ResourceManager
- An **ApplicationMaster** that's created for each application to negotiate for resources and work with the NodeManager to execute and monitor tasks
- Resource containers that are controlled by NodeManagers and assigned the system resources allocated to individual applications

### 5. See the output

First of all, go the fileviewer from localhost:8080 :
    
<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1kMviTSOGYtcyGSKNbgZ7wOs3cp44qmLY">
</p>

Go to user > raj_ops > TP > output and click on `part-r-00000` to view the file :

You should see something like this :

```
"#Muscular	1
"'Come	1
"'Dieu	1
"'Dio	1
"'From	1
"'Grant	1
"'I	4
"'No	1
...
"Anna	2
"Annette,	1
"Announce	1
"Another	7
"Any	2
"Anybody	1
"Anyhow	1
"Anyhow,	2
"Anything	1
"Appeal	1
"Apropos,	1
"Arakcheev	1
"Are	30
"Aren't	2
"Arguing?	1
"Arinka!	1
"Arnauts!"	1
"Arrange	1
"Arranging	1
"Arthur	1
"As	36
```
