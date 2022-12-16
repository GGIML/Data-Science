FROM python:3.7-slim-stretch

# Install wget
RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

# Install cloudsql proxy
#RUN mkdir /cloudsql
#RUN mkdir /build
#RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O /build/cloud_sql_proxy
#RUN chmod +x /build/cloud_sql_proxy

# Install dependencies
ADD requirements.txt ./
RUN python -m pip install -r requirements.txt

COPY mlflow-vivadata-268120-0f8e7cd0d135.json ./mlflow-vivadata-268120-0f8e7cd0d135.json

ADD startup-vivadata.sh ./startup.sh
RUN chmod +x ./startup.sh

ENTRYPOINT ./startup.sh
