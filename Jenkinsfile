properties([
                            parameters([
                                [$class: 'ChoiceParameter', 
                                    choiceType: 'PT_SINGLE_SELECT', 
                                    description: 'Select the docker image from the Dropdown List', 
                                    filterLength: 1, 
                                    filterable: false, 
                                    name: 'docker_image', 
                                    script: [
                                    $class: 'ScriptlerScript',
                                    scriptlerScriptId:'fetchJsonDataFromGithub.groovy',
                                    parameters: [
                                      [name:'owner', value: 'RouachedHoussemEddine'],
                                      [name:'repo', value: 'sbm_test'],
                                      [name:'branch', value: 'test'],
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
