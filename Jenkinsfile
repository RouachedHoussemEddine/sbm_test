pipeline {
    agent {
        docker {
            image 'python:3.10.5'
        }
    }
    stages {
        stage('Pull GitHub') {
            steps {
                checkout(
                    scm: git(
                        branches: [[name: '**']],
                        userRemoteConfigs: [[url: 'https://github.com/RouachedHoussemEddine/sbm_test']]
                    )
                )
            }
        }
        stage('Build Docker image') {
            steps {
                script {
                    def param1Value = params.docker_image
                    sh "echo Value of docker_image: ${param1Value}"
                    sh "docker build --build-arg PARAM1=${param1Value} -t sbm_test src/."
                }
            }
        }
    }
}
