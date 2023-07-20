parameters([
                    choice(name:"NeedUpgradePC",choices:['yes','no'],description: "Do you need upgrade your PC"),
                    
                    [$class: 'DynamicReferenceParameter',
                            choiceType: 'ET_FORMATTED_HTML',
                            omitValueField: true,
                            description: 'Please provide a Elastic alias label',
                            name: 'PC_RAM',
                            randomName: 'choice-parameter-5631314456178624',
                            referencedParameters: 'NeedUpgradePC',
                            script: [
                                    $class: 'GroovyScript',
                                    fallbackScript: [
                                            classpath: [],
                                            sandbox: true,
                                            script:
                                                    'return[\'nothing.....\']'
                                    ],
                                    script: [
                                            classpath: [],
                                            sandbox: true,
                                            script:
                                                    """
                                    if(NeedUpgradePC.equals('yes')) {
                                        inputBox="<input name='value' type='text' value='Kingston 8GB'>"
                                    } else {
                                        inputBox="<input name='value' type='text' value='Kingston 8GB' disabled>"
                                    }
                                """
                                    ]
                            ]
                         ],
                        
                        [$class: 'DynamicReferenceParameter',
                                    choiceType: 'ET_FORMATTED_HTML',
                                    omitValueField: true,
                                    description: 'Please provide a Elastic alias label',
                                    name: 'PC_CPU',
                                    randomName: 'choice-parameter-5631314456178624',
                                    referencedParameters: 'NeedUpgradePC',
                                    script: [
                                            $class: 'GroovyScript',
                                            fallbackScript: [
                                                    classpath: [],
                                                    sandbox: true,
                                                    script:
                                                            'return[\'nothing.....\']'
                                            ],
                                            script: [
                                                    classpath: [],
                                                    sandbox: true,
                                                    script:
                                                            """
                                    if(NeedUpgradePC.equals('yes')) {
                                        inputBox="<input name='value' type='text' value='Intel Core i5'>"
                                    } else {
                                        inputBox="<input name='value' type='text' value='Intel Core i5' disabled>"
                                    }
                                """
                                            ]
                                    ]
                            ]

            ])

pipeline {
    agent any
    stages {
        stage('Pull GitHub') {
            steps {
                checkout scmGit(branches: [[name: "*/test"]], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RouachedHoussemEddine/sbm_test']])
            }
        }
        
        stage('Fetch Docker image information') {
            steps {
                script {
                    def branchSpecificJson = sh(returnStdout: true, script: "curl -s https://raw.githubusercontent.com/RouachedHoussemEddine/sbm_test/test/sbm.json")
                    def json = readJSON(text: branchSpecificJson)
                    def dockerImage = json.docker_image
                    def dockerImageVersion = json.docker_image_version_python
                    echo "Docker Image: ${dockerImage}"
                    echo "Docker Image Version: ${dockerImageVersion}"
                }
            }
        }
        
        stage('Build Docker image') {
            steps {
                script {
                    def dockerImage = sh(returnStdout: true, script: "echo ${dockerImage}").trim()
                    def dockerImageVersion = sh(returnStdout: true, script: "echo ${dockerImageVersion}").trim()
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
