
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
                bat '''
                "C:\\Users\\Sharvil\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt
                '''
            }
        }

        stage('Build') {
            steps {
                bat '''
                "C:\\Users\\Sharvil\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m compileall -q app.py
                '''
            }
        }

        stage('Automated Tests') {
            steps {
                bat '''
                "C:\\Users\\Sharvil\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest -v
                '''
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t student-management:v1 .'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                docker rm -f student-app 2>NUL
                docker run -d --name student-app -p 5000:5000 student-management:v1
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Application built, tested, and deployed!'
            echo 'Open http://localhost:5000'
        }

        failure {
            echo 'FAILURE: Check the Console Output for the failed stage.'
        }

        always {
            echo 'Student Management CI/CD Pipeline completed.'
        }
    }
}
