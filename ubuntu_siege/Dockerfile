#This is intended to ping an nginx container on the server

FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y siege python

COPY siege.py /

CMD ["python", "siege.py"]