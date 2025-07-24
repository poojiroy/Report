pipeline {
    agent any

    environment {
        IMAGE_NAME = "weather-api"
        CONTAINER_NAME = "weather-app"
        PORT = "5000"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                echo "Running unit tests inside Docker..."
                sh 'docker run --rm $IMAGE_NAME:latest pytest'
            }
        }

        stage('Stop Old Container') {
            steps {
                echo "Stopping old container..."
                sh 'docker stop $CONTAINER_NAME || true && docker rm $CONTAINER_NAME || true'
            }
        }

        stage('Run New Container') {
            steps {
                echo "Running new container..."
                sh 'docker run -d -p $PORT:5000 --name $CONTAINER_NAME $IMAGE_NAME:latest'
            }
        }
    }
}
