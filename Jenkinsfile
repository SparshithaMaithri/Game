pipeline {
    agent any

    environment {
        // ✅ Full PATH includes Docker, Kubectl, Git, Python, Node, and Windows tools
        PATH = "C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Windows\\System32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files\\Git\\cmd;C:\\Program Files\\nodejs\\;C:\\Program Files\\Python312\\Scripts\\;C:\\Program Files\\Python312\\;${PATH}"
        KUBECONFIG = "C:\\Users\\spmah\\.kube\\config"
    }

    stages {
        stage('Verify Docker & Kubectl') {
            steps {
                echo "🐳 Checking Docker and Kubectl..."
                bat '''
                docker --version
                kubectl version --client
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🏗️ Building Docker Image..."
                dir('C:\\Users\\spmah\\Downloads\\Game') {
                    bat 'docker build -t kubdemoapp:v1 .'
                }
            }
        }

        stage('Docker Login') {
            steps {
                echo "🔐 Logging into Docker Hub..."
                bat 'docker login -u sparshitha -p 0213@Csptha'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "🚀 Pushing Docker Image to Docker Hub..."
                bat '''
                docker tag kubdemoapp:v1 sparshitha/game:kubeimage1
                docker push sparshitha/game:kubeimage1
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "⚙️ Deploying to Kubernetes cluster..."
                bat '''
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
