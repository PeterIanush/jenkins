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
                    label 'MASTER'
                }
            }
            steps {
                sh 'mkdir -p /var/logs/geocitizen/logs/'
		sh 'nohup mvn -f $(PROJECT_PATH)/pom.xml clean install >> $(DEPLOY_LOG)'
            }
        }
        
        
        stage('Build') {
            agent {
                node {
                    label 'MASTER'
                }
            }
            options {
                retry(2)
                timestamps()
            }
            steps {
					script {
                                            if (fileExists ('$(PROJECT_PATH)/target/citizen.war')) {
                                                    sh 'rm -rf /usr/local/tomcat9/webapps/citizen.war'
						    sh 'rm -rf /usr/local/tomcat9/webapps/citizen'
						    sh 'cp $PROJECT_PATH/target/citizen.war /usr/local/tomcat9/webapps/'
                                            } else {
						sh 'nohup  mvn -f $PROJECT_PATH/pom.xml clean install -DskipTests >> $DEPLOY_LOG'
						sh 'rm -rf /usr/local/tomcat9/webapps/citizen.war'
						sh 'rm -rf /usr/local/tomcat9/webapps/citizen'
						sh 'cp $PROJECT_PATH/target/citizen.war /usr/local/tomcat9/webapps/fi'
													
													
                                            }
                                    }
                
            }
	    always{
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
        }
        
        stage('Cleanup') {
            agent {
                node {
                    label 'MASTER'
                }
            }
            
            }
            steps {
                sh 'mvn clean'
            }
        }
        
    }   


