#!/bin/bash
log_file="/opt/airflow/log.txt"
current_time=$(TZ='Asia/Seoul' date '+%Y-%m-%d %H:%M:%S')
echo "[$current_time] ---- AIRFLOW USER 생성 로그 시작 ----" >> $log_file
# airflow 유저 생성 로그 정보 기록
output=$(python /opt/airflow/create_airflow_user.py 2>&1)
echo "[$current_time] Script Output:" >> $log_file
echo "$output" >> $log_file
echo "[$current_time] ---- AIRFLOW USER 생성 로그 완료 ----" >> $log_file
echo "[$current_time] ---- 도커 PORT 체크 시작 ----" >> $log_file
output=$(python /opt/airflow/port_check.py 2>&1)
echo "[$current_time] Script Output:" >> $log_file
echo "$output" >> $log_file
echo "[$current_time] ---- 도커 PORT 체크 완료 ----" >> $log_file
# 파이썬 패키지 설치
nohup pip install --no-cache-dir -r python_package_install.txt 
echo "[$current_time] ---- 파이썬 패키지 설치 시작 대상 : /opt/airflow/Longtime_python_package_install.txt 확인, 로그 파일 : /opt/airflow/Longtime_python_package_install.log  ----" >> $log_file
nohup pip install --no-cache-dir -r /opt/airflow/Longtime_python_package_install.txt > /opt/airflow/python_package_install.log 2>&1 &
echo "[$current_time] ---- 파이썬 패키지(오래 걸리는 부분) 설치 진행중 로그 : /opt/airflow/python_package_install.log  ----" >> /opt/airflow/Longtime_python_package_install.log 
