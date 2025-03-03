pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git credentialsId: 'github-token', url: 'https://github.com/Leype83936222/CLoud_iot.git', branch: 'main'
            }
        }
    }
}
