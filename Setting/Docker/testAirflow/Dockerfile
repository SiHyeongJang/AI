FROM apache/airflow:2.1.2-python3.8

# Switch to root user for additional package installations
USER root

# Update the package list and install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    vim \
    procps \
    && apt-get autoremove -yqq --purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set a password for the airflow user (replace 'password' with your desired password)
RUN echo 'airflow:airflow' | chpasswd

# Add user 'default' with sudo privileges
RUN useradd -m default
RUN echo "default ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/default
RUN chmod 0440 /etc/sudoers.d/default

COPY init_airflow.sh /home/airflow/init_airflow.sh
RUN chmod +x /home/airflow/init_airflow.sh

# Switch back to the airflow user
CMD ["bash"]
