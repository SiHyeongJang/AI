import os
import logging
from dotenv import load_dotenv
from airflow import settings
from airflow.utils.db import create_session
from airflow.www.security import AirflowSecurityManager
from airflow.www.app import create_app
from datetime import datetime

# .env 파일에서 환경 변수 로드
load_dotenv()

AIRFLOW_ID = os.getenv('AIRFLOW_ID')
AIRFLOW_PW = os.getenv('AIRFLOW_PW')
AIRFLOW_EMAIL = os.getenv('AIRFLOW_Email')

# 로그 설정
log_file_path = '/opt/airflow/log.txt'
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s %(message)s')

def create_airflow_user(username, password, email):
    app = create_app()
    security_manager = app.appbuilder.sm

    with create_session() as session:
        user = security_manager.find_user(username=username)
        if user:
            message = f"User '{username}' already exists."
            print(message)
            logging.info(message)
            return

        role_admin = security_manager.find_role('Admin')
        user = security_manager.add_user(
            username=username,
            first_name='FIRST_NAME',
            last_name='LAST_NAME',
            email=email,
            role=role_admin,
            password=password
        )
        if user:
            message = f"User '{username}' created successfully."
            print(message)
            logging.info(message)
        else:
            message = f"Failed to create user '{username}'."
            print(message)
            logging.info(message)

create_airflow_user(AIRFLOW_ID, AIRFLOW_PW, AIRFLOW_EMAIL)

