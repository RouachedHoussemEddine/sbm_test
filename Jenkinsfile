pipeline {
    agent any

    stages {
        stage('pull github') {
            steps {
                checkout scmGit(branches: [[name: '**']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RouachedHoussemEddine/sbm_test']])
            }
        
            
            
        }
        stage('build docker image') {
            steps{
                
                sh 'docker build --tag sbm_test src/.'
            }
        }
    }
}
