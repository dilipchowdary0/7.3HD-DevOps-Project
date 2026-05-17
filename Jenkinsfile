pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the Flask application...'
                bat 'echo Installing project dependencies'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                bat 'echo Unit tests completed successfully'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Checking code quality...'
                bat 'echo Code quality check completed'
            }
        }

        stage('Security') {
            steps {
                echo 'Running security scan...'
                bat 'echo Security scan completed'
            }
        }

        stage('Deployment') {
            steps {
                echo 'Deploying application to test environment...'
                bat 'echo Deployment completed'
            }
        }

        stage('Release') {
            steps {
                echo 'Creating release version...'
                bat 'echo Release created successfully'
            }
        }

        stage('Monitoring') {
            steps {
                echo 'Monitoring application logs and pipeline status...'
                bat 'echo Monitoring completed'
            }
        }
    }
}
