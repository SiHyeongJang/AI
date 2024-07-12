import os
import socket
import dotenv

# .env 파일 로드
dotenv_path = '/opt/airflow/.env'
if not os.path.exists(dotenv_path):
    print(f"에러 !! {dotenv_path} 파일을 찾을 수 없습니다.")
    exit(1)

dotenv.load_dotenv(dotenv_path)

# 테스트할 포트 변수 목록 및 대응하는 호스트 변수 이름
port_variables = {
    ('AIRFLOW_IN', 'AIRFLOW_PORT'): 'AIRFLOW_HOSTNAME',
    ('JUPYTER_PORT_IN', 'JUPYTER_PORT'): 'AIRFLOW_HOSTNAME',
    ('POSTGRE_PORT', 'POSTGRE_PORT'): 'POSTGRESQLDB_HOSTNAME',
    ('ZOOKEEPER_PORT', 'ZOOKEEPER_PORT'): 'ZOOKEEPER_HOSTNAME',
    ('KAFKA1_PORT', 'KAFKA1_PORT'): 'KAFKA1_HOSTNAME',
    ('KAFKA2_PORT', 'KAFKA2_PORT'): 'KAFKA2_HOSTNAME',
    ('KAFKA3_PORT', 'KAFKA3_PORT'): 'KAFKA3_HOSTNAME',
    ('kafka_ui_IN', 'kafka_ui'): 'KAFKAUI_HOSTNAME'
}

# 포트 핑 테스트 함수
def ping_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # 1초 타임아웃
    try:
        sock.connect((host, port))
    except socket.error:
        return False
    sock.close()
    return True

# 메인 테스트 로직
for (external_port_var, internal_port_var), host_var in port_variables.items():
    external_port = os.getenv(external_port_var)  # 외부 포트 환경 변수 값
    internal_port = os.getenv(internal_port_var)  # 내부 포트 환경 변수 값
    host = os.getenv(host_var, "localhost")  # 호스트 환경 변수 값 (없으면 기본값 localhost)

    external_port_result = False
    internal_port_result = False

    if external_port:
        try:
            external_port = int(external_port)  # 외부 포트를 정수로 변환
            external_port_result = ping_port(host, external_port)  # 외부 포트 핑 테스트
        except ValueError:
            print(f"에러 !! {external_port_var}에 대한 유효하지 않은 포트 번호: {external_port}")

    if internal_port:
        try:
            internal_port = int(internal_port)  # 내부 포트를 정수로 변환
            internal_port_result = ping_port(host, internal_port)  # 내부 포트 핑 테스트
        except ValueError:
            print(f"에러 !! {internal_port_var}에 대한 유효하지 않은 포트 번호: {internal_port}")

    if external_port_result or internal_port_result:
        print(f"호스트: {host}, 포트 {external_port if external_port_result else internal_port}에 연결할 수 있습니다.")
    else:
        print(f"에러 !!: 포트 {external_port} ({external_port_var}) 및 {internal_port} ({internal_port_var})에 연결할 수 없습니다. 호스트: {host}, 확인이 필요합니다.")

