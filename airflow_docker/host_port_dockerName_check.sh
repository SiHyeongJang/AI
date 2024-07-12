#!/bin/sh

# .env 파일 경로 설정
ENV_FILE=".env"

# 확인할 포트 변수 목록
PORT_VARS="AIRFLOW_PORT JUPYTER_PORT POSTGRE_PORT ZOOKEEPER_PORT KAFKA1_PORT KAFKA2_PORT KAFKA3_PORT kafka_ui"

# .env 파일에서 포트 값을 읽고 확인
if [ -f "$ENV_FILE" ]; then
    for VAR in $PORT_VARS; do
        PORT=$(grep -oP "$VAR=\K\d+" "$ENV_FILE")
        if [ -n "$PORT" ]; then
            if ss -tuln | grep -q ":$PORT"; then
                echo "포트 $PORT ($VAR) 는 사용 중입니다."
            else
                echo "포트 $PORT ($VAR) 는 사용 중이지 않습니다."
            fi
        else
            echo "$VAR 값이 .env 파일에 설정되어 있지 않습니다."
        fi
    done
else
    echo ".env 파일을 찾을 수 없습니다."
    exit 1
fi


# 검색할 변수들을 정의합니다
NAME_VARS="AIRFLOW_HOSTNAME POSTGRESQLDB_HOSTNAME ZOOKEEPER_HOSTNAME KAFKA1_HOSTNAME KAFKA2_HOSTNAME KAFKA3_HOSTNAME KAFKAUI_HOSTNAME"

# docker ps -a --format "{{.Names}}" 명령어의 출력 저장
docker_names=$(docker ps -a --format "{{.Names}}")

# 각 변수를 검색하여 출력 및 중복 체크합니다
for var in $NAME_VARS; do
    # 변수 값을 .env 파일에서 추출하고, 줄바꿈을 제거합니다
    value=$(grep "^$var=" "$ENV_FILE" | cut -d '=' -f2- | tr -d '\r' | tr -d '\n')

    if [ -z "$value" ]; then
        echo "$var not found or has no value in .env file"
    else
        echo "DEBUG: $var 값: '$value'"
        # docker 컨테이너 목록에서 변수 값이 존재하는지 확인
        if echo "$docker_names" | grep -qw "$value"; then
            echo "$var 값인 '$value'이(가) docker 컨테이너 목록에 존재합니다."
        else
            echo "$var 값인 '$value'이(가) docker 컨테이너 목록에 존재하지 않습니다."
        fi
    fi
done

