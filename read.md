# Python Hello World Application on Kubernetes

This is a simple guide to help you create a Python Hello World application and deploy it on Kubernetes. By following these steps, you will be able to containerize your Python application, create a Docker image, and deploy it on a Kubernetes cluster.

## Prerequisites
- Python installed on your local machine
- Docker installed on your local machine
- A Kubernetes cluster up and running (e.g., Minikube or a cloud provider's Kubernetes service)

## Steps

### 1. Create a Python Application
Start by creating a simple Python application that prints "Hello, World!". Create a new file named `app.py` and add the following code:

```python
print("Hello, World!")
```

### 2. Containerize the Python Application
To run the Python application on Kubernetes, we need to containerize it using Docker. Create a new file named `Dockerfile` (without any extension) and add the following content:

```Dockerfile
# Use the official Python image as the base image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the container
COPY app.py .

# Run the Python application when the container starts
CMD ["python", "app.py"]
```

### 3. Build and Push the Docker Image
Next, build the Docker image for your Python application and push it to a container registry. Open a terminal and navigate to the directory where the `Dockerfile` and `app.py` files are located. Run the following commands:

```bash
# Build the Docker image
docker build -t your-image-name .

# Tag the Docker image (optional, if using a remote registry)
docker tag your-image-name your-registry/your-image-name

# Push the Docker image (optional, if using a remote registry)
docker push your-registry/your-image-name
```

Make sure to replace `your-image-name` with a suitable name for your Docker image, and `your-registry` with the address of your container registry (e.g., Docker Hub or a private registry).

### 4. Deploy the Python Application on Kubernetes
Now it's time to deploy the Python application on Kubernetes. Create a new file named `deployment.yaml` and add the following content:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: your-deployment-name
spec:
  replicas: 1
  selector:
    matchLabels:
      app: your-app-name
  template:
    metadata:
      labels:
        app: your-app-name
    spec:
      containers:
      - name: your-container-name
        image: your-registry/your-image-name
        ports:
        - containerPort: 80
```

Again, make sure to replace `your-deployment-name`, `your-app-name`, `your-container-name`, and `your-registry/your-image-name` with appropriate values.

Save the `deployment.yaml` file.

### 5. Deploy the Deployment
Use the Kubernetes command-line tool (`kubectl`) to deploy the application. Run the following command:

```bash
kubectl apply -f deployment.yaml
```

### 6. Verify the Deployment
To ensure that the deployment is successful, you can check the status of the deployed pods using the following command:

```bash
kubectl get pods
```

You should see a pod with a name similar to `your-deployment-name-xxxxxxxxxx-xxxxx` in the `Running` state.

### 7. Access the Python Application
To access the Python application, you need to expose it as a Kubernetes service. Create a new file named `service.yaml` and add the following content:

```

yaml
apiVersion: v1
kind: Service
metadata:
  name: your-service-name
spec:
  selector:
    app: your-app-name
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: NodePort
```

Replace `your-service-name` and `your-app-name` with suitable values. Save the `service.yaml` file.

### 8. Deploy the Service
Deploy the service using the following command:

```bash
kubectl apply -f service.yaml
```

### 9. Access the Application
To access the Python application, you need to get the URL of the exposed service. Run the following command:

```bash
minikube service your-service-name --url
```

If you're using Minikube, it will display the URL for accessing your application. If you're using a different Kubernetes cluster, refer to the documentation to find the appropriate command for accessing the service.

Open the URL in a web browser, and you should see the "Hello, World!" message printed.

Congratulations! You have successfully created a Python Hello World application and deployed it on Kubernetes.

## Conclusion
In this guide, you learned how to create a simple Python Hello World application, containerize it using Docker, and deploy it on a Kubernetes cluster. You also learned how to expose the application as a service and access it. Feel free to explore more advanced topics like scaling, load balancing, and deploying more complex Python applications on Kubernetes. Happy coding!
