
pipeline {
    agent any

    stages {
        stage('Docker Image Build') {
            steps {
                echo 'Building..'
                sh 'uname -a'
                sh 'whoami'
                sh 'usermod -aG docker jenkins' 
                sh 'docker build -t luke4egg/phase3:latest .'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

