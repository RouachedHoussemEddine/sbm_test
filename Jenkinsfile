pipeline {
    agent any
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
            steps{ 
                script {
                    def param1Value = params.docker_image
                    sh "echo Value of ACTIVE_PARAM1: ${param1Value}"
                    sh "docker build --build-arg PARAM1=${param1Value} -t sbm_test src/."
                }
            }
        }
    }
}
