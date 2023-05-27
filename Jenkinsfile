pipeline {
  agent any
  stages {
    stage('cat-go') {
      steps {
        sh 'cat main.go'
      }
    }

    stage('cat-python') {
      steps {
        sh 'ca main.py'
      }
    }

  }
}