# Challenge - GCP Setup

![](https://images.unsplash.com/photo-1419833173245-f59e1b93f9ee?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)
Picture by [Sam Schooler](https://unsplash.com/photos/E9aetBe2w40)

## Objectives

- Create your Azure and/or GCP account.
- Launch a virtual machine and connect it with SSH / Browser SSH.
- Same as before, deploy your Docker Recommender App.

## Guidelines

##### Create your account
- You will need to create your account and provide your billing informations, even if you only use free services.

Go to : https://cloud.google.com/ and open the console.

##### Push your docker image to Docker Hub

From the folder of your app:
```bash
docker images
```

Make sure you are logged-in in Docker. If not, create a Docker Hub account, and run:

```bash
docker login --username=yourhubusername --email=youremail@company.com
```

To check if you are logged in, `docker login` should return "Login Succeeded".

Tag your image accordingly (use the image ID from `docker images`):

```bash
docker tag <image ID> <yourusername>/app:latest
```

And push it !

```bash
docker push <yourusername>/app:latest
```

After the upload, it will be available from your Hub, and anyone will be able to pull it (expect if you make it private. This 1st private is free, then you have to pay :) )

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1x_gD6gSYRj-DDd_LcPPzpSxjtob59eqw">
</p>

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1f_Z5g_Bh8e249pD5FQTXVMMeCh_Z32Vv">
</p>

##### Create a VM Instance on GCP

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1Chh_IUbmmDOIgim43N0rmpAoNgr7P2Rk" style="width: 400px;">
</p>

Enable billing if needed. Don't worry, the VM we'll create is specialized for containers and will cost around 0.034 dollar / hour over you 300$ of free credits :) And we'll delete it after a few minutes.

##### Check the button "Deploy a container image to this VM instance

This will select a specialized VM instance (Container-Optimized OS), pre-install docker and run your VM for you !

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1fkoudp6Wv7AQr0jvI3tVMlIbgSee47wB" style="width: 800px;">
</p>

This will select a specialized VM instance (Container-Optimized OS), pre-install docker and run your VM for you !

Then, make sure to allow HTTP traffic to connect to the instance.

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=19oZ6aubEF3iB-7etF22ioBWK0NHla8Ru" style="width: 800px;">
</p>

##### Access your work online !

And this is it ! To access your web app, simply copy-paste its external IP (XX.XXX.XXX.XXX) and if you need a special port (other than 80 and 443), you'll need to add a firewall rule.

Your Netflix Webapp sends information on port 5000. We just need to create a specific network rule that states that you can listen to port 5000. This is by default de-activated to avoid making all your work available.

First, go to VPC Network -> Firewall rules.

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=15y2-G4EIMSjcSASwWx_NRc-lRWBoyNXx">
</p>

Then, click on "Create new Firewall rule". Fill it in this way :

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1CkTLsj5ANj3VPimT7C_iF4V7IifYbRkp">
</p>

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1mNq5NF7IZN8JOaQrnBWesNfbRLdDxhZU">
</p>

Your app is now available on the equivalent address:

http://XX.XX.XXX.XXX:5000/

##### Check your Docker Image

GCP offers a terminal to access the instance and check its content. First, from the instance home page, click on SSH to establish SSH connection to the instance.

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=12XJE_h1pz66VynDn0ul0HNp40XRAjhZa">
</p>

Finally, you can verify that the image is present and that the container is up and running !

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1u7pj8dBqu2FPEkpgCsmH4d5Dvi05J2Hy">
</p>

You can also monitor your instance by clicking on it, and then on "Monitor".

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1jqVQIqk6kkFEg9umenJ6wKhaUjxe3a7l">
</p>

## <p style="color:Tomato;">Make sure you stop or delete every service on GCP !</p>
