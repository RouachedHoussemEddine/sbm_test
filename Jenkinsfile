properties([
  parameters([
      [
      $class: 'ChoiceParameter',
      choiceType: 'PT_SINGLE_SELECT',
      name: 'BRANCH_NAME',
      // description:  'Cluster ?',
      // referencedParameters: 'CLUSTER',
        fallbackScript: [
                    classpath: [],
                    sandbox: false,
                    script: "return['Could not get The environments']"
                ],
                script: [
                    classpath: [],
                    sandbox: false,
                    script: "return['dev','stage','prod']"
                ]
      ]
      ,
      [
      $class: 'DynamicReferenceParameter',
      choiceType: 'ET_FORMATTED_HTML',
      name: 'Kong_Parameters',
      referencedParameters: 'BRANCH_NAME',
      script: [
          $class: 'ScriptlerScript',
          scriptlerScriptId:'fetchJsonDataFromGithub.groovy',
          // sandbox: true,
          parameters: [
            [name:'owner', value: "RouachedHoussemEddine"],
            [name:'repo', value: 'sbm_test'],
            [name:'branch', value: 'test'],
            [name:'filePath', value: 'sbm.json'],
            [name:'parameter', value: 'docker_image']
          ]
        ],
      omitValueField: false,
      ]
      
   ])
 ])


pipeline {
    agent any

    parameters {
        choice(name: 'Branch name', choices: "${BRANCH_NAME}", description: 'Branch to build')



   stages {
        stage('Pull GitHub') {
            steps {
                checkout scmGit(branches: [[name: "*/${params.BRANCH_NAME}"]], extensions: [], userRemoteConfigs: [[url: 'https://github.com/RouachedHoussemEddine/sbm_test']])
            }
        }
        
        stage('Fetch Docker image information') {
            steps {
                script {
                    def branchSpecificJson = sh(returnStdout: true, script: "curl -s https://raw.githubusercontent.com/RouachedHoussemEddine/sbm_test/${params.BRANCH_NAME}/sbm.json")
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
}