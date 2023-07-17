pipeline {
    agent any
    
    parameters {
        choice(name: 'BRANCH_NAME', choices: ['test', 'dev', 'prod'], description: 'Branch to build')
        choice(name: 'DOCKER_IMAGE', choices: ['image1', 'image2'], description: 'Docker image to use')
        choice(name: 'DOCKER_IMAGE_VERSION', choices: ['v1', 'v2'], description: 'Version of the Docker image')
    }
    
    stages {
        stage('Pull GitHub') {
            steps {
                checkout scmGit(branches: [[name: "*/${params.BRANCH_NAME}"]], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RouachedHoussemEddine/sbm_test']])
            }
        }
        
        stage('Build Docker image') {
            steps {
                script {
                    def dockerImage = params.DOCKER_IMAGE
                    def dockerImageVersion = params.DOCKER_IMAGE_VERSION
                    sh "docker build --build-arg PARAM1=${dockerImage} --build-arg PARAM2=${dockerImageVersion} -t sbm_test src/."
                }
            }
        }
    }
    
    post {
        success {
            // Actions to perform on successful build
            echo 'Build succeeded!'
        }
        
        failure {
            // Actions to perform on failed build
            echo 'Build failed!'
        }
    }
}
