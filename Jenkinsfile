pipeline {
    agent any

    environment {
        ACR_NAME = 'webappacr'
        IMAGE_NAME = 'python-webapp'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jojinjoseph/python-webapp2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }
        stage('Push to ACR') {
            steps {
                script {
                    withEnv(["DOCKER_CONTEXT=default"]) {   // Add this line
                        docker.withRegistry("https://${ACR_NAME}.azurecr.io", 'webappacr') {
                        docker.image("${IMAGE_NAME}").push()
                    }
                }
        }
    }
}


        stage('Deploy to AKS') {
            steps {
                withCredentials([file(credentialsId: 'aks-kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'kubectl apply -f deployment.yaml'
                    sh 'kubectl apply -f service.yaml'
                }
            }
        }
    }
}
