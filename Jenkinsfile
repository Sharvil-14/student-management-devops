
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
                bat '''
                "C:\\Users\\Sharvil\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t student-management:v1 .
                '''
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                "C:\\Users\\Sharvil\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" rm -f student-app 2>NUL
                "C:\\Users\\Sharvil\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run -d --name student-app -p 5000:5000 student-management:v1
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Build, tests, and deployment completed.'
        }

        failure {
            echo 'FAILURE: Check the stage that failed in Console Output.'
        }

        always {
            echo 'Student Management CI/CD pipeline finished.'
        }
    }
}
