pipeline {
     agent {
        docker {
            // Specify the Docker image to use
            image 'python:3.10.5'
        }
    parameters {
        // Define the parameters you want to pass to the build
        string(name: 'PARAM1', defaultValue: ${docker_image} , description: 'Description of PARAM1')
    }
    stages {
        stage('pull github') {
            steps {
                checkout scmGit(branches: [[name: '**']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RouachedHoussemEddine/sbm_test']])
            }
        
        }
        stage('build docker image') {
            steps{   
                sh 'docker build --build-arg PARAM1=${params.PARAM1} -t sbm_test src/.'
            }
        }
    }
}
