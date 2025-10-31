pipeline {
    agent any

    environment {
        // Add Docker path so Jenkins can access it
        PATH = "${PATH};C:\\Program Files\\Docker\\Docker\\resources\\bin"
    }

    stages {
        stage('Check Docker') {
            steps {
                echo '🔍 Checking Docker installation...'
                bat 'docker --version'
                bat 'docker ps'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker Image..."
                dir('C:\\Users\\spmah\\Downloads\\Game') {
                    bat 'docker build -t kubdemoapp:v1 .'
                }
            }
        }

        stage('Docker Login') {
            steps {
                echo "🔑 Logging into Docker Hub..."
                bat 'docker login -u sparshitha -p 0213@Csptha'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "🚀 Pushing Docker image to Docker Hub..."
                bat 'docker tag kubdemoapp:v1 sparshitha/game:kubeimage1'
                bat 'docker push sparshitha/game:kubeimage1'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "⚙️ Deploying to Kubernetes cluster..."
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
