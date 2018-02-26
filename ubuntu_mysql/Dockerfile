#This is intended to ping an nginx container on the server

FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y mysql-client python iputils-ping

COPY mysql_query_container.py /

CMD ["python", "mysql_query_container.py"]