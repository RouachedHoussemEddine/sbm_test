@Library('docker-workflow@master') _
properties([                            
    parameters([

        choice (choices: getGithubInfoByKey('GitHub_owner'), description: 'Provide GitHub owner', name: 'GitHub_owner'),
        choice (choices: getGithubInfoByKey('Repository'), description: 'Provide GitHub repository', name: 'Repository'),
        choice (choices: getGithubInfoByKey('Branch'), description: 'Provide GitHub branch', name: 'Branch'),
        choice (choices: getGithubInfoByKey('jsonfilelocation'), description: 'Provide jsonfile name', name: 'jsonfile'),
                [$class: 'CascadeChoiceParameter', 
                    choiceType: 'PT_SINGLE_SELECT', 
                    description: 'Select the docker image',  
                    name: 'docker_image',
                    referencedParameters: 'GitHub_owner,Repository,Branch,jsonfile',
                    script: [
                    $class: 'ScriptlerScript',
                    scriptlerScriptId:'fetchJsonDataFromGithub.groovy',
                    parameters: [
                    [name:'owner', value: '${GitHub_owner}'],
                    [name:'repo', value: '${Repository}'],
                    [name:'branch', value: '${Branch}'],
                    [name:'filePath', value: '${jsonfile}'],
                    [name:'parameter', value: 'docker_image']
                    ]
                    ]
                ]
                ,
                [$class: 'CascadeChoiceParameter', 
                    choiceType: 'PT_SINGLE_SELECT', 
                    description: 'Select docker image version from the List',
                    name: 'docker_image_version', 
                    referencedParameters: 'docker_image,GitHub_owner,Repository,Branch,jsonfile', 
                    script: [
                    $class: 'ScriptlerScript',
                    scriptlerScriptId:'fetchJsonDataFromGithubVersion.groovy',
                    parameters: [
                    [name:'owner', value: '${GitHub_owner}'],
                    [name:'repo', value: '${Repository}'],
                    [name:'branch', value: '${Branch}'],
                    [name:'filePath', value: '${jsonfile}'],
                    [name:'parameter', value: '${docker_image}']
                    ]
                    ]
                ]
                ,
                [$class: 'CascadeChoiceParameter', 
                    choiceType: 'PT_SINGLE_SELECT', 
                    description: 'Select the  AMI  information', 
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

def getGithubInfoByKey(String dataKey) {
    def githubPath = 'https://raw.githubusercontent.com/RouachedHoussemEddine/sbm_test/test/sbm.json'
    def jsonData = new URL(githubPath).getText()
    def parsedJson = new groovy.json.JsonSlurper().parseText(jsonData)
    return parsedJson."${dataKey}".join('\n')
}

pipeline {
    agent any

environment {
    DOCKERHUB_CREDENTIALS = credentials('DOCKERHUB_CREDENTIALS_ID_TEST')
  }

    stages {
        stage('Fetch JSON data from GitHub') {
            steps {
                script {  
                def user = params.GitHub_owner
                def repo = params.Repository
                def branch = params.Branch
                def jsonFileLocation = params.jsonfile
                // Construct the GitHub path to the JSON file
                //def githubPath = "https://raw.githubusercontent.com/RouachedHoussemEddine/sbm_test/test/sbm.json"
                // Fetch JSON data from the repository and store it as a file
                sh 'curl -o sbm.json https://raw.githubusercontent.com/RouachedHoussemEddine/sbm_test/test/sbm.json'
                    }
                }
        }
        
        
        
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
            sh "docker build --build-arg PARAM1=${param1Value} --build-arg PARAM2=${param2Value} -t sbm_test src/."
                }
            }

        }

        stage('Push Docker image to Docker Hub') {
                    steps {
                        script {
                            withCredentials([usernamePassword(credentialsId: 'DOCKERHUB_CREDENTIALS_ID_TEST', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                                sh "echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin"
                                    def dockerHubUsername = "azzinoth5"
                                    def repo = params.Repository
                                    def dockerHubRepo = "${dockerHubUsername}/${repo}" 
                                    def dockerHubTag = "v1.0" //desired tag/version
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