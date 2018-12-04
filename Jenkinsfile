peline {
        agent none
        options {

        }
        tools{

        }
        stages{
                stages('hello-world'){
                        agent{
							node{
								lable 'local-server'
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
