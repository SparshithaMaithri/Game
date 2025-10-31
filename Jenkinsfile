pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                // Navigate to your project folder
                dir('C:\\Users\\spmah\\Downloads\\Game') {
                    bat "docker build -t kubdemoapp:v1 ."
                }
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub..."
                bat 'docker login -u sparshitha -p 0213@Csptha'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker Image to Docker Hub..."
                bat "docker tag kubdemoapp:v1 sparshitha/game:kubeimage1"
                bat "docker push sparshitha/game:kubeimage1"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes cluster..."
                bat '''
                set KUBECONFIG=C:\\Users\\spmah\\.kube\\config
                kubectl cluster-info
                kubectl apply -f C:\\Users\\spmah\\Downloads\\Game\\deployment.yaml
                kubectl apply -f C:\\Users\\spmah\\Downloads\\Game\\service.yaml
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check Jenkins logs for details.'
        }
    }
}
