#FROM apache/airflow:2.1.2-python3.8
FROM apache/airflow:slim-2.8.1-python3.10

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    vim \
    procps \
    expect \
    && apt-get autoremove -yqq --purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 환경 변수 설정
ENV AIRFLOW_HOME=/opt/airflow
ENV JUPYTER_CONFIG_DIR=/opt/airflow/.jupyter

RUN echo 'airflow:airflow' | chpasswd
RUN echo "airflow ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/default
RUN chmod 0440 /etc/sudoers.d/default

COPY init_airflow.sh /home/airflow/init_airflow.sh
COPY start_jupyter.sh /home/airflow/start_jupyter.sh
COPY create_airflow_user.py .

RUN chmod +x /home/airflow/init_airflow.sh /home/airflow/start_jupyter.sh

USER airflow

RUN pip install --no-cache-dir jupyter notebook psycopg2-binary python-dotenv

# Jupyter 설정 파일 생성 및 설정 추가
RUN mkdir -p $JUPYTER_CONFIG_DIR && \
    jupyter notebook --generate-config --allow-root && \
    echo "c.NotebookApp.allow_root = True" >> $JUPYTER_CONFIG_DIR/jupyter_notebook_config.py && \
    echo "c.NotebookApp.token = ''" >> $JUPYTER_CONFIG_DIR/jupyter_notebook_config.py && \
    echo "c.NotebookApp.ip = '0.0.0.0'" >> $JUPYTER_CONFIG_DIR/jupyter_notebook_config.py && \
    echo "c.NotebookApp.port = 8888" >> $JUPYTER_CONFIG_DIR/jupyter_notebook_config.py

# 작업 디렉토리 설정
WORKDIR $AIRFLOW_HOME

COPY python_package_install.txt .
COPY Longtime_python_package_install.txt .
COPY .env .
COPY port_check.py .
COPY 2start.sh .

CMD ["bash"]
