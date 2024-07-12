import os
from notebook.auth import passwd

# 환경 변수에서 패스워드 가져오기
jupyter_password = os.getenv('JUPYTER_PASSWORD')

# 패스워드 해시 생성
password_hash = passwd(jupyter_password)

# Jupyter 설정 파일 경로
jupyter_config_file = '/root/.jupyter/jupyter_notebook_config.py'

# 설정 파일에 설정 추가
with open(jupyter_config_file, 'a') as f:
    f.write(f"c.NotebookApp.password = '{password_hash}'\n")

