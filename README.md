# BerkeleyProject

Project is developed in macOS environment

## App

<img width="510" alt="Screenshot 2020-05-09 at 9 53 58 PM" src="https://user-images.githubusercontent.com/21097132/81475657-26847a80-9240-11ea-87a3-79b64bf963fb.png">


## Quick Start to start service in Docker

1. Make sure you have Python 2.7 and Docker installed
2. Clone with this project into your preferred application directory
3. Run docker-compose build to build the image
4. Run docker-compose up to start the application

Application should be running at localhost in browser


## Deploy in Kubernetes locally (Re-use the app and DockerFile from above)

1. Setup kuberctl : `brew install kubectl` and follow instruction to make kubectl to executable
2. Setup minikube : `brew install minikube`
3. Execute `minikube start`
4. Go to the root directory of the project and execute `eval $(minikube docker-env)` to setup docker environment
5. Built the image in the environment to allow image to be pulled locally `docker-compose build`
6. Verify that images is now in the docker environment `docker images`
7. Start the application deployment  `kubectl create -f ./deploy/deploy.yml`
8. Check status of the pod `kubectl get pods`, ensure that the status is `Running`
9. Start the kubernetes service to allow us to access the deployed kubernetes cluster `kubectl create -f /deploy/service.yml`
10. Check the config is correct `kubectl get svc`  
11. Obtain the IP to allow local machine to access the application `kubectl describe pods | grep Node: | awk -F '/' '{print $2}'`
12. Access the application via a browser at `IP:30000` (30000 is set in the service.yml file)


## Future work
1. Connect to an external redis rather a shared redis to allow service to be load-balanced in different pods
2. Build and push image to a local registry rather than building the image in the minikube docker environment
3. Edit `/etc/hosts` with the IP of the kubernetes service and deploy an nginx to port forward the request to 30000 instead of explicitly setting the port number in the url. 

## Stack
- Frontend: HTML
- Backend: Django
- Cache: Django_redis
- Orchestrator: Kubernetes
