pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''#!/bin/bash
                echo 'In C or Java, we can compile our program in this step'
                echo 'In Python, we can build our package here or skip this step'
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''#!/bin/bash
                echo 'Test Step: Running pytest using conda environment'

                # Initialize conda environment (replace PATH with your actual conda path)
                /home/team02/miniconda3/condabin/conda init bash

                # Activate the conda environment and run pytest
                /home/team02/miniconda3/condabin/conda run -n mlip pytest

                # Exit with 1 for failure if pytest fails
                if [ $? -ne 0 ]; then
                  exit 1
                fi
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'In this step, we deploy our project'
                echo 'Depending on the context, we may publish the project artifact or upload pickle files'
            }
        }
    }
}
