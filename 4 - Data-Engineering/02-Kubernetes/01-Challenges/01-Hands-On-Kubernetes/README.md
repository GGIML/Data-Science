# Challenge - Kubernetes learning hands-on

![](https://images.unsplash.com/photo-1570129477492-45c003edd2be?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80)

## 0. Installation

You need a local kubernetes cluster during the challenges.

Please install and configure your computer:
- install [minikube](https://kubernetes.io/fr/docs/setup/learning-environment/minikube/) or [docker-desktop](https://www.docker.com/products/docker-desktop)
- install [kubectl](https://kubernetes.io/fr/docs/reference/kubectl/cheatsheet/)
- create an alias *k for kubectl*
- configure the auto-completion
- install [kubectx and kubens](https://github.com/ahmetb/kubectx)

## 1. Create your namespace

In order to practice in the cluster and to keep the cluster neat, please create your namespace and set it as the current one.

## 2. Deploy a Hello world pod

Create a pod, based on a simple image (busybox), display "Hello vivadata!" at the start-up of the pod

## 3. Deployment of the application california-housing-app

- Step 1: Create a deployment with the image california-housing-app and set the replica to 4 instances, listening on the port 5000
- Step 2: Delete a pod and check what happens
- Step 3: Reduce the replica to 2

## 4. Create a NodePort service to the application

In order to get access to the application from your computer:

- Step 1: Create a NodePort service listening on the port 31000.
- Step 2: Open a browser and go the application
- Step 3: Check the logs of the deployment
