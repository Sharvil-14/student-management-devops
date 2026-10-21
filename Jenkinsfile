
stage('Install Dependencies') {
    steps {
        bat '"C:\\Users\\Sharvil\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
    }
}

stage('Build') {
    steps {
        bat '"C:\\Users\\Sharvil\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m compileall -q app.py'
    }
}

stage('Automated Tests') {
    steps {
        bat '"C:\\Users\\Sharvil\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest -v'
    }
}
