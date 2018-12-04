pipeline {

        agent none
        stages{
                stage('hello-world'){
                        agent{
                                                        node{
                                                                label 'master'
                                                        }

                        }
                                                option{
                                                        retry(2)
                                                }
                                                steps {
                                                        folder('HelloWorld')
                                                        sh 'touch HelloWorld >> echo "Hello Peter"'
                                                }


                }
        }
}
