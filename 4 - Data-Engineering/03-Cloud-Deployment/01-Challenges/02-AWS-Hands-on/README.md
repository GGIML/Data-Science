# Challenge - AWS Hands-on

![](https://images.unsplash.com/photo-1419833173245-f59e1b93f9ee?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)
Picture by [Sam Schooler](https://unsplash.com/photos/E9aetBe2w40)

## Create an AWS folder for this session

### Create your account
- You will need to create your account and provide your billing informations, even if you only use free services.
- Create AWS folder to keep your access keys.

## 1. Quick start with EC2

### 1.1 Create EC2 key, security group

In this part we will create two things :
- A **key-pair**, this is a simple key to access an EC2 machine
- A **security-group**, this is a set of rules for authorizing and blocking traffic going in/out of your EC2 machine.

##### Create EC2 access key-pair

- Open up the [EC2 Management Console](https://eu-west-1.console.aws.amazon.com/ec2/v2/home?region=eu-west-1#Home:) in **Services** > **Calcul** > **EC2**
- On the left pane, go to **Paires de clés** in **Réseau & Securité**
- **Créer une paire de clés**, and name it : *vivakey*
- The key is automatically downloaded, keep it in your AWS folder

For security, it is important to modify the read access of the key, if you don't, AWS will tell you to do it. 

- Open a terminal in your AWS folder and run :

> `chmod 400 vivakey.pem`

##### Our default security group

We will modify our default security group so that we can play with EC2 without access problems.

- In the left pane, we will go in the left pane, **Groupes de sécurité**
- We will modify the rule for the group named **default**
- Right click and go in **modify inboud rules** we need to have this :

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1AS36CmFlcEbxEMreXbrMACINcTflGB2E">
</p>

- If you go in **modify outbound rules** we need to have this :

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1-MZKKxu8D352C_QWfPjiYnmMj1GFmAhi">
</p>

That's it ! Now you also have a specific key for accessing your EC2 instances, and a security group which lets you play around. Let's create an instance.

### 1.2 Create your EC2 Instance

Creating your Elastic Cloud Compute instance with the AWS console is pretty simple, it is composed of few steps :

Virtual servers for general purpose computing. Launch an instance in 5 steps :

##### 🛒Choose instance OS Image (Ex. Ubuntu, Amazon Linux, Custom Images..)

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1H2ewa8n-m3ZnQsfXkZL6CQRYqxHn0xHd">
</p>

##### 🛒Choose instance type (from t2.micro 🐢 >> m5b.32xlarge 🐇)

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1XEB3nmvr4u1syCVlsbABe9eg9PFOHsE-">
</p>

💡Some powerful instances are restricted, you have to ask AWS to modify your quotas

##### ⚙️Configure instance (sub-network, user roles, storage volumes)

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1DjW_moEXPsG4vfgOqCadfY9yNozw399x">
</p>

💡 Instances Spot

##### Add some storage and balises (optional)

##### 🔐Configure security group (network filters)

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=13UfVhGw0KRBknr7WJ2-i0e54XUeVHzzi">
</p>

##### 🗝Review the instance and choose your access key

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1mKCDW0qlx4eWSIxWBtRiLgurjz7kPiGq">
</p>

You can now **launch** your EC2 instance and get the connection adress when it is ready.
The **DNS Public** address is important, you will connect to the instance with this address.

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1X-DOjq018wA7DpaM4Vl2M0ZapM4MFvk2">
</p>

### 1.3 Access your EC2 instance

Now that we have set the access key, security groupand the instance, we can connect to it with this command :

> `ssh -i vivakey.pem ubuntu@public-dns-address`



### 1.4 Install docker on your instance

With the following commands, you can install docker on your instance :

Swith to super-user :
> `sudo su`

Do some updates on your system :
> `apt-get update`

> `apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common`

Add the docker repository :
> `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`

> `add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`

Install and test Docker :
> `apt-get install -y docker-ce docker-ce-cli containerd.io`

> `docker run hello-world`

### 1.5 Run your netflix recommandation app

We will directly pull your netflix app docker-image.

You can use this for retrieving the netflix-app image from docker hub :

> `sudo docker pull <yourusername>/vivadata:first`

Now you can launch your container with your app :

> `sudo docker run -p 5000:5000 <yourusername>/vivadata:first`

To access it, use in browser : **http://ec2-ipv4-adress:5000**

## 2. Quickstart with AWS Command Line

### 2.1 Create IAM user

Access security is very important on AWS, it is important to think about the permissions when using the services. We will create a username to use the AWS Command Line Interface, and access services such as ec2 and s3.

- Open up the [IAM Service Console](https://console.aws.amazon.com/iam/home#/home)
- Go to **Utilisateurs** > **Ajouter un utilisateur**
- Step 1 is the **username**, we want a progammatic access to the ressources (first box, Command Line)
- Step 2 is **authorizations**, we will create a new group named **admin**, and give it **AdministratorAccess**, this group has no limitations.
- Step 3 **Balises** is optional, here you can specify some user information, you can try adding context:test-vivadata.
- Step 4 is a **summary** of your user info and authorizations.
- At Step 5 you must **download your user credentials** in a CSV file.

This is it, you have created a user with administrator rights. You will use it with the command line interface.

### 2.2 Setting up the AWS CLI

##### Install AWS CLI

> `pip install awscli --upgrade --user`

##### Test your install

> `aws help`

##### Setting up your credentials
> `aws configure`

This line will ask you some lines to identify your account. Here you will use the credentials of the user we created earlier, the one with admin access (the CSV file in your AWS folder).
- AWS Access Key : The 'access key' part of your credentials.
- AWS Secret Access Key : The 'secret' part of your credentials.
- Default region name : Working region, **eu-central-1** (✋✋✋ ⚠️ Use the same region as the one you're displaying on AWS!)
- Default output format : [text]

### 2.3 AWS command line examples
```aws [options] <command> <subcommand> [parameters]```

##### Some examples

- Create a key pair, used fo accessing instances :

```aws ec2 create-key-pair --key-name MyKeyPair```

- Create a security group, used to group some machines together :

```aws ec2 create-security-group --group-name <sec-group-name> --description "My security group" --vpc-id <ip-of-existing-vpc>```

- Create an EC2 instance :

`aws ec2 run-instances --image-id <os-image-ami-id>`

`aws ec2 run-instances --image-id <os-image-ami-id> --instance-type t2.micro --key-name vivakey --security-groups default`

- Shutting down one or more instances :

```aws ec2 terminate-instances --instance-ids <instance-id> --key-name <key-pair-name> --security-groups-ids <sec-group-id> --instance-type t2.micro```

## 3. S3 - Simple Storage Quickstart

Now that we have setup our AWS Command Line, we will use it to play with the S3 service.

### 3.1 Create a bucket with the console

Creating a bucket is really simple, in the [S3 Management console](https://s3.console.aws.amazon.com/s3/home?region=eu-central-1#) you hit **Créer un compartiment**. 

Then, all you have to do is provide a **unique bucket name**, make it realy specific, but not too complicated. You don't have to touch any other settings, and you get your private bucket. When created, you can finally add your files via the management console.

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1UNLQ4ChDmj8xBSeXB5hlWGmbICdhq9Eo">
</p>

### 3.2 Use the AWS Command line to interact with buckets ⌨️

##### To create and delete buckets, you use the **aws s3api** client :

You can **create a bucket** from your command line with :

> `aws s3api create-bucket --bucket <change-to-unique-name> --region eu-west-1 --create-bucket-configuration LocationConstraint=eu-west-1`

You can also **kill a bucket** with the command line :

> `aws s3api delete-bucket --bucket change-to-unique-name`

You can find more in the [docs](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html).

##### To manipulate files in a specific bucket, you use the **aws s3** client : 

To play with your bucket, you can use commands like **ls, mv, cp...** as explained in the [docs](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html)

Check the files in a bucket :

> `aws s3 ls s3://unique-bucket-name/`

Add a local file to your bucket :

> `aws s3 cp archive.tar s3://unique-bucket-name/subfolder/`

## <p style="color:Tomato;">Make sure you delete every service on AWS !</p>