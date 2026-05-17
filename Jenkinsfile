pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the Flask application...'
                bat 'py -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                bat 'py -m pytest'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Checking code quality...'
                bat 'py -m compileall .'
            }
        }

        stage('Security') {
            steps {
                echo 'Running security check...'
                bat 'py -m pip list'
            }
        }

        stage('Deployment') {
            steps {
                echo 'Deploying application to test environment...'
            }
        }

        stage('Release') {
            steps {
                echo 'Creating release version...'
            }
        }

        stage('Monitoring') {
            steps {
                echo 'Monitoring application logs and pipeline status...'
            }
        }
    }
}
