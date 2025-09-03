pipeline {
    agent any
    environment {
        VENV_DIR = "venv"
        FLASK_PORT = "5000"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Creating Python virtual environment and installing dependencies...'
                sh 'python3 -m venv $VENV_DIR'
                sh '$VENV_DIR/bin/pip install --upgrade pip'
                sh '$VENV_DIR/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                echo 'Starting Flask app in background...'
                // Start Flask using venv Python, run in background, save PID
                sh "nohup $VENV_DIR/bin/python app.py & echo \$! > app.pid"
                // Wait for Flask to start
                sleep 8
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium tests with pytest...'
                sh "$VENV_DIR/bin/pytest tests/ --maxfail=1 --disable-warnings -q"
            }
        }
    }

    post {
        always {
            echo 'Cleaning up Flask app process...'
            // Kill Flask app process if it exists
            sh 'if [ -f app.pid ]; then kill $(cat app.pid) || true; fi'
        }
        success {
            echo 'Pipeline finished successfully!'
            emailext(
                to: 'aahanshetye.stu@gmail.com',
                subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Python Selenium pipeline executed successfully: ${env.BUILD_URL}"
            )
        }
        failure {
            echo 'Pipeline failed!'
            emailext(
                to: 'aahanshetye.stu@gmail.com',
                subject: "FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Python Selenium pipeline failed: ${env.BUILD_URL}"
            )
        }
    }
}
