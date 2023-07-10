pipeline {
    agent any
    
    stages {
        stage('Pull GitHub') {
            steps {
                    checkout scmGit(branches: [[name: '**']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RouachedHoussemEddine/sbm_test']])
            }
        }
        stage('Build Docker image') {
            steps {
                script {
                    def param1Value = params.docker_image
                    def param2Value = params.docker_image_version
                    sh "echo Value of docker_image: ${param1Value}"
                    sh "echo Value of docker_image_version: ${param2Value}"
                    sh "docker build --build-arg PARAM1=${param1Value} PARAM2=${param2Value} -t sbm_test src/."
                }
            }
        }
    }
}
