# RESTful-microservice

## Assignment Specifications
1. An operational application with minimal functionality.
2. Ability to communicate with the application through REST, preferably with Swagger integration.
3. Implementation of basic functionality to handle the four REST commands: GET, POST, PUT, DELETE.
4. Containerization of the application using Docker, facilitated by a Dockerfile.
5. Organization of all source code within a private GitHub repository.

## Build and Run Instructions
Use the following terminal commands to:
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/meganrallen/RESTful-microservice
3. Navigate to the project directory: cd <project-directory>
4. Build the Docker image:
   ```bash
   docker build -t mallen5/rest:v0.0.1 .
5. Apply ConfigMap:
   ```bash
   kubectl apply -f ConfigMap.yaml
6. Apply Deployment:
   ```bash
   kubectl apply -f deployment.yaml
7. Apply Service:
   ```bash
   kubectl apply -f service.yaml
8. Verify Deployments, Pods, Services, and ConfigMaps are running:
   ```bash
   kubectl get deployments
   kubectl get pods
   kubectl get services
   kubectl get configmaps
10. Access the microservice externally using NodePort and capture the output:
    ```bash
    curl http://34.42.155.186:31234/config > curl_config.txt
    curl http://34.42.155.186:31234/fib?length=10 > curl_fib.txt
11. [Optional] Access Swagger UI documentation: http://localhost:5000/swagger

## Learning Journey
1. Installed necessary dependencies for the Visual Studio Code development environment.
2. Understood and visualized the assignment requirements based on the specified specifications.
3. Utilized provided resources, including documentation such as Flask-RESTful Quickstart Guide, to create the foundational code for the microservice.
4. Debugged and troubleshooted issues encountered during development to ensure the functionality of the microservice.
5. Experimented with Docker to containerize the application, understanding its concepts and usage in the context of this project.

## Sources
1. Flask-RESTful Quickstart Guide: https://flask-restful.readthedocs.io/en/latest/
2. Claude AI and ChatGPT
