pipeline {
    agent any

    environment {
    	SRC_DIR = 'project'
    }

    stages {
        stage('Build') {
            steps {
                echo "Building ${env.JOB_NAME}"
            }
        }
        stage('Test') {
            steps {
	        echo 'Testing'
            	sh 'python -m pytest || true'
		echo 'Linting'
		sh "pylint ${env.SRC_DIR}"
	    }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}