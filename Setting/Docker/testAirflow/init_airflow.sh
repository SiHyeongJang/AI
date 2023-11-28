#!/bin/bash

# Wait for PostgreSQL to be ready
sleep 10

# Initialize Airflow database
airflow db init

# Install additional packages if needed
pip install --no-cache-dir airflow-code-editor

# Create an admin user for Airflow
airflow users create \
    --username admin \
    --firstname FIRST_NAME \
    --lastname LAST_NAME \
    --role Admin \
    --password admin \
    --email tlgud4175@gmail.com

# Start the Airflow webserver and scheduler
exec airflow webserver & airflow scheduler

