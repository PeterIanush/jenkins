pipeline {

        agent none
        stages{
                stage('hello-world'){
                        agent{
							node{
								lable 'master'
							}
                        
                        }
						option{
							retry(2)
						}
						steps {
							folder('HelloWorld')
							touch HelloWorld >> echo "Hello Peter"
						}
						
						
                }
        }
}
