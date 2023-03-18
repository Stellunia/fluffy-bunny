/* Requires the Docker Pipeline plugin */
pipeline {
  agent any
  stages {
    stage('Testing GitHub-tests locally') {
      steps {
        dir('C:/Users/Stella/gitproject/fluffy-bunny/SIDE Exports/Successful tests'){
          bat 'python -m unittest'
        }
      }
   }
    stage('Clean Workspace'){
      steps {
        cleanWs()
      }
    }
  }
}
