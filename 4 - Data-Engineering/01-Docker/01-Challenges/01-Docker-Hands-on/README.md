# Challenge - Docker learning hands-on

![](https://images.unsplash.com/photo-1493946740644-2d8a1f1a6aff?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1368&q=80)
Picture by [frank mckenna](https://unsplash.com/photos/tjX_sniNzgQ)

## Installation

You will be using docker-cli (ie. Command line interface, your terminal) mostly.
Make sure you have **docker-ce** and **docker-cli** installed, refer to the documentation of your operating system.

## 1. Hello world

The most common first step is Hello World ! Docker also comes with an Hello World container !

- Find the hello-world command and run it.
- Take some time to read that output.

## 2. Launch a containerized python 2 prompt

- With the ```docker run``` command, launch an ephemeral python2 container, and access its prompt.
> ```docker run -it python:2```
- Have a look at the documentation for **docker run**, find what **-it** is for.
- Launch the python prompt.
- Test some commands to validate it is python2 (the **print** command is different than py3)

Hint : Think about the image-name:version for the container

## 3. Simple image for Python app with libraries

For this exercise we will build a Dockerfile step by step for a basic python container.

- Create a docker-test folder (with mkdir linux command)
- Create a file : requirements.txt - This file will be read by pip for installing various libraries.
- Add on each line : numpy, pandas, scikit-learn
- requirements.txt should look like :
	**numpy**
	**pandas**
	**scikit-learn**
- Create a new file named 'Dockerfile' and complete it :
- See example of a Dockerfile in the next exercise
	- (FROM) Use latest ubuntu as base image
	- (RUN) Add update command : `apt-get update -y`
	- (RUN) Add install command : `apt-get install -y python3-pip python3-dev build-essential`
	- (COPY) Add files to the container : "COPY . ." (how do you understand this command ?)
	- (RUN) Add pip3 command for requirements : `pip3 install -r requirements.txt`

- Open a terminal in your docker-test folder, it must contain your Dockerfile and requirements.txt
- Build the docker image with the ```docker build``` command. Give the tag python-simple with latest version [See docs for docker build](https://docs.docker.com/engine/reference/commandline/build/)
- Use . at the end of your command to use the files in the current folder.

At this point you have built a docker image, you can check this with the command ```docker images```.

- Now launch a container with this image, just like Question2, you just have to change image name and version.

## 4. Let's Dockerize your California Housing app

We will now dockerize your California Housing prediction application. Create a new folder (outside of your Vivadata folder), and copy-paste your application in the folder (make sure to include everything). Our aim is now to create the requirements and the Dockerfile for your application.

- Step 1 : Create a directory with your app files, Dockerfile, and requirements.txt
- Step 2 : List the libraries used in your project and put them in requirements.txt
- Step 3 : For the Dockerfile :

```bash
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . .
RUN pip3 install -r requirements.txt
# Launch app
ENTRYPOINT ["python3", "main.py"]
```

- Step 4 : Build your docker image with ```docker build```, name it 'california' for example. Don't forget to place your terminal in your working directory and use . to include all files.

- Step 5 : Launch a container of your california image. You will have to specify the -p option for the Flask port 5000 : "-p 5000:5000"

- Step 6 : Open up your browser and check localhost:5000 !
