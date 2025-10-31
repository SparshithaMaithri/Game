pipeline {
  agent any

  stages {
    stage('Check Docker') {
      steps {
        bat 'where docker || (echo "docker not found" & exit 1)'
        bat 'docker --version'
      }
    }

    stage('Build Docker Image') {
      steps {
        dir('C:\\Users\\spmah\\Downloads\\Game') {
          bat 'docker build -t kubdemoapp:v1 .'
        }
      }
    }

    stage('Docker Login') {
      steps {
        // avoid plaintext in pipeline - use Jenkins credentials in real pipelines
        bat 'docker login -u sparshitha -p 0213@Csptha'
      }
    }

    stage('Push Docker Image') {
      steps {
        bat 'docker tag kubdemoapp:v1 sparshitha/game:kubeimage1'
        bat 'docker push sparshitha/game:kubeimage1'
      }
    }

    stage('Deploy to K8s') {
      steps {
        bat '''
          set KUBECONFIG=C:\\Users\\spmah\\.kube\\config
          kubectl apply -f C:\\Users\\spmah\\Downloads\\Game\\deployment.yaml
          kubectl apply -f C:\\Users\\spmah\\Downloads\\Game\\service.yaml
        '''
      }
    }
  }

  post {
    success { echo '✅ Pipeline completed' }
    failure { echo '❌ Pipeline failed' }
  }
}
