script {
    STATUS_PATH = '/var/jenkins/dumb-slave-1/workspace/status/'
    PROJECT_PATH='/usr/local/projects/Geocitizen'
    DEPLOY_LOG='/var/logs/geocitizen/logs/deploy.log'
}

pipeline {
    agent none

stages {
    stage('LOCAL') {
        agent {
            node {
                label 'master'
            }
        }
        steps {
            sh 'mkdir -p /var/logs/geocitizen/logs/'
	    
            sh 'sudo mvn -f /usr/local/projects/Geocitizen/pom.xml install -DskipTests'
        }
    }


    stage('Build') {
        agent {
            node {
                label 'master'
            }
        }
        options {
            retry(2)
            timestamps()
        }
        steps {
                script {
                    if (fileExists ('/usr/local/projects/Geocitizen/target/citizen.war')) {
                            sh 'rm -rf /usr/local/tomcat9/webapps/citizen.war'
                            sh 'rm -rf /usr/local/tomcat9/webapps/citizen'
                            sh 'cp /usr/local/projects/Geocitizen/target/citizen.war /usr/local/tomcat9/webapps/'
                    } else {
                        sh 'mvn -f /usr/local/projects/Geocitizen/pom.xml clean install -DskipTests'
                        sh 'rm -rf /usr/local/tomcat9/webapps/citizen.war'
                        sh 'rm -rf /usr/local/tomcat9/webapps/citizen'
                        sh 'cp /usr/local/projects/Geocitizen/target/citizen.war /usr/local/tomcat9/webapps/'


                    }
                }

        }
        
        post {
                failure {
                        mail subject: "${currentBuild.fullDisplayName} FAILURE",
                        body: "${env.BUILD_URL}",
                        to: 'petiayanush@gmail.com, petiaianush@gmail.com'
                }
                success {
                        mail subject: "${currentBuild.fullDisplayName} SUCCESS",
                        body: "${env.BUILD_URL}",
                        to: 'petiayanush@gmail.com, petiaianush@gmail.com'
                        }

        }
        
    }

    stage('Cleanup') {
        agent {
            node {
                label 'MASTER'
            }
        }
	steps {
            sh 'mvn clean'
        }
        }
        
    }

}
