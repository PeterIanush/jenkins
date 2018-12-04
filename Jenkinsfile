pipeline {

        agent none
        stages{
                stage('hello-world'){
                        agent{
                                                        node{
                                                                label 'master'
                                                        }

                             }
                                                steps {
                                                        
                                                        sh 'touch HelloWorld'
							sh 'echo "Hello Peter >> Helloworld"'
                                                }


                }
        }
}
