pipeline {
     agent {
        docker {
            // Specify the Docker image to use
            image 'python:3.10.5'
        }
    stages {
        stage('pull github') {
            steps {
                checkout scmGit(branches: [[name: '**']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RouachedHoussemEddine/sbm_test']])
            }
        
        }
        stage('build docker image') {
            steps{ 
                def param1Value = params.docker_image
                sh "echo Value of ACTIVE_PARAM1: ${param1Value}"
                sh 'docker build --build-arg PARAM1=${param1Value} -t sbm_test src/.'
            }
        }
    }
    }
}