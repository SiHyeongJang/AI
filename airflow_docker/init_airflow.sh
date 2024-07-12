#!/bin/bash

# 포스트그리 실행 대기
sleep 10
#!/bin/bash
airflow db init || echo "$(date '+%Y-%m-%d %H:%M:%S') 데이터베이스 초기화 실패하여 기존 db 폴더로 진행합니다. db 초기화를 원할 시 db 폴더를 삭제 후 진행" >> log.txt


# .env 파일에서 환경 변수 로드
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# expect 스크립트 실행
# 명령 결과 처리

# 에러 핸들링

pip install --no-cache-dir airflow-code-editor

# create_airflow_user.py 스크립트 실행 및 로그 출력
# create_airflow_user.py 스크립트 실행 및 로그 출력

# Create an admin user for Airflow using expect

# Initialize Airflow database
# Airflow 설정 파일 경로 설정
AIRFLOW_CFG_PATH="/opt/airflow/airflow.cfg"  

# 변경할 시간대 값 설정
NEW_TIMEZONE="Asia/Seoul"
# 변경할 executor 값 설정
NEW_EXECUTOR="LocalExecutor"

# 설정 파일에서 default_timezone 값 변경
sed -i "s%^default_timezone = .*%default_timezone = $NEW_TIMEZONE%" $AIRFLOW_CFG_PATH
# 설정 파일에서 default_ui_timezone 값 변경
sed -i "s%^default_ui_timezone = .*%default_ui_timezone = $NEW_TIMEZONE%" $AIRFLOW_CFG_PATH
# 설정 파일에서 executor 값 변경
sed -i "s%^executor = .*%executor = $NEW_EXECUTOR%" $AIRFLOW_CFG_PATH

echo "Airflow 설정 파일의 default_timezone, default_ui_timezone, executor 값을 $NEW_TIMEZONE, $NEW_TIMEZONE, $NEW_EXECUTOR로 변경하였습니다."

# Start the Airflow webserver and scheduler
#airflow webserver & airflow scheduler & jupyter notebook --no-browser --ip 0.0.0.0 --allow-root
airflow webserver & airflow scheduler



