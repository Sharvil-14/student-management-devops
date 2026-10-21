
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
