pipeline {
    agent any
    stages {
        stage('preparation') {
            steps {
                // Get some code from a GitHub repository
                git 'https://github.com/mahmoud254/jenkins_nodejs_example.git'
            }
        }
        stage('CI') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'password', usernameVariable: 'username')]) {
                   // Get some code from a GitHub repository
                   sh """sudo docker build . -f dockerfile -t abdelrahmanzaki179/docker_with_jenkins_ex:latest
                    sudo docker login -u ${username} -p ${password}
                    sudo docker push abdelrahmanzaki179/docker_with_jenkins_ex:latest
                   """
                }
            }
        }
        stage('CD') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'password', usernameVariable: 'username')]) {
                   // Get some code from a GitHub repository
                   sh """
                    sudo docker login -u ${username} -p ${password}
                    sudo docker run -p 3000:3000 -d abdelrahmanzaki179/docker_with_jenkins_ex:latest
                   """
                }
            }
        }
    }
}
