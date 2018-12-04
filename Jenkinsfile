pipeline {

        agent none
        stages{
                stages('hello-world'){
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
						}
						steps {
							touch HelloWorld >> echo "Hello Peter"
						}
                }
        }
}
