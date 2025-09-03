pipeline {
    agent any
    environment {
        VENV_DIR = "venv"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh '. $VENV_DIR/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run App') {
            steps {
                sh 'nohup . $VENV_DIR/bin/activate && python app.py & echo $! > app.pid'
                sleep 5  // wait for Flask app to start
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '. $VENV_DIR/bin/activate && pytest tests/ --maxfail=1 --disable-warnings -q'
            }
        }
    }

    post {
        always {
            sh 'if [ -f app.pid ]; then kill $(cat app.pid) || true; fi'
        }
    }
}
