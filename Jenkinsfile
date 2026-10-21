
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                bat 'python -m compileall -q app.py'
            }
        }

        stage('Automated Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t student-management:v1 .'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker rm -f student-app || exit /b 0'
                bat 'docker run -d --name student-app -p 5000:5000 student-management:v1'
            }
        }
    }
}
