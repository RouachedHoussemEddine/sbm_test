properties([
                            parameters([
                                //  choice(name: 'BRANCH_NAME', choices: ['test', 'dev', 'prod'], description: 'Branch to build')
                                choice (choices: ['RouachedHoussemEddine', 'sbm', 'zied'], description: 'Provide GitHub owner', name: 'GitHub_owner'),
                                choice (choices: ['sbm_test', 'projet_Auth', 'projet_Park'], description: 'Provide GitHub repository', name: 'Repository'),
                                choice (choices: ['test', 'dev', 'prod'], description: 'Provide GitHub branch', name: 'Branch'),
                                [$class: 'CascadeChoiceParameter', 
                                    choiceType: 'PT_SINGLE_SELECT', 
                                    description: 'Select the docker image from the Dropdown List',  
                                    name: 'docker_image',
                                    referencedParameters: 'GitHub_owner,Repository,Branch',
                                    script: [
                                    $class: 'ScriptlerScript',
                                    scriptlerScriptId:'fetchJsonDataFromGithub.groovy',
                                    parameters: [
                                      [name:'owner', value: '${GitHub_owner}'],
                                      [name:'repo', value: '${Repository}'],
                                      [name:'branch', value: '${Branch}'],
                                      [name:'filePath', value: 'sbm.json'],
                                      [name:'parameter', value: 'docker_image']
                                      ]
                                    ]
                                ],
                                [$class: 'CascadeChoiceParameter', 
                                    choiceType: 'PT_SINGLE_SELECT', 
                                    description: 'Select the AMI from the Dropdown List',
                                    name: 'docker_image_version', 
                                    referencedParameters: 'docker_image', 
                                    script: [
                                    $class: 'ScriptlerScript',
                                    scriptlerScriptId:'fetchJsonDataFromGithubVersion.groovy',
                                    parameters: [
                                      [name:'owner', value: 'RouachedHoussemEddine'],
                                      [name:'repo', value: 'sbm_test'],
                                      [name:'branch', value: 'test'],
                                      [name:'filePath', value: 'sbm.json'],
                                      [name:'parameter', value: '${docker_image}']
                                      ]
                                    ]
                                ],
                                [$class: 'CascadeChoiceParameter', 
                                    choiceType: 'PT_SINGLE_SELECT', 
                                    description: 'Select the  AMI based on the following information', 
                                    name: 'Image Information', 
                                    referencedParameters: 'docker_image', 
                                    script: 
                                        [$class: 'GroovyScript', 
                                        fallbackScript: [
                                                classpath: [], 
                                                sandbox: false, 
                                                script: "return['Could not get Environment from Env Param']"
                                                ], 
                                        script: [
                                                classpath: [], 
                                                sandbox: false, 
                                                script: '''
                                                if (docker_image.equals("python")){
                                                    return["ami-sd2345sd", "ami-asdf245sdf", "ami-asdf3245sd"]
                                                }
                                                else if(docker_image.equals("nginx")){
                                                    return["ami-sd34sdf", "ami-sdf345sdc", "ami-sdf34sdf"]
                                                }
                                                else if(docker_image.equals("busybox")){
                                                    return["ami-sdf34sdf", "ami-sdf34ds", "ami-sdf3sf3"]
                                                }
                                                else if(docker_image.equals("postgres")){
                                                    return["ami-sdf34sdf", "ami-sdf34ds", "ami-sdf3sf3"]
                                                }
                                                '''
                                            ] 
                                    ]
                                ]
                            ])
                        ])

def pushDockerImageToDockerHub() {
    script {
        def dockerHubRepo = "azzinoth5/sbm_test" // Replace <DOCKERHUB_USERNAME> with your Docker Hub username
        def dockerHubTag = "v1.0" // Replace v1.0 with the desired tag/version

        // Log in to Docker Hub
        docker.withRegistry(url: 'https://registry.hub.docker.com', credentialsId: 'DOCKERHUB_CREDENTIALS_ID') {
            sh "docker tag sbm_test ${dockerHubRepo}:${dockerHubTag}"
            sh "docker push ${dockerHubRepo}:${dockerHubTag}"
        }
    }
}



pipeline {
    agent any
    stages {
        stage('Pull GitHub') {
            steps {
                checkout scmGit(branches: [[name: "*/test"]], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RouachedHoussemEddine/sbm_test']])
            }
        }
        
        stage('Build Docker image') {
            steps {
                script {
                    def param1Value = params.docker_image
                    def param2Value = params.docker_image_version
                    //sh "echo Value of docker_image: ${param1Value}"
                    //sh "echo Value of docker_image_version: ${param2Value}"
                    sh "docker build --build-arg PARAM1=${param1Value} --build-arg PARAM2=${param2Value} -t sbm_test src/."
                }
            }

        }
        stage('Push Docker image to Docker Hub') {
                    steps {
                        script {
                            withCredentials([usernamePassword(credentialsId: 'DOCKERHUB_CREDENTIALS_ID_TEST', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                                sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                            }
                                def dockerHubUsername = "azzinoth5"
                                def repo = "sbm_test"
                                def dockerHubRepo = "${dockerHubUsername}/${repo}" // Replace <DOCKERHUB_USERNAME> with your Docker Hub username
                                def dockerHubTag = "v1.0" // Replace v1.0 with the desired tag/version
                                docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                                    sh "docker tag sbm_test ${dockerHubRepo}:${dockerHubTag}"
                                    sh "docker push ${dockerHubRepo}:${dockerHubTag}"
                                    sh "docker logout"
                                    }
                                
                                
                               
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