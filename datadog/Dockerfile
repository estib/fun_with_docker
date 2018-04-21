FROM datadog/agent:latest

ADD elastic.yaml /etc/datadog-agent/conf.d/elastic/auto_conf.yaml
ADD mysql.yaml /etc/datadog-agent/conf.d/mysql.d/conf.yaml
ADD nginx.yaml /etc/datadog-agent/conf.d/nginx.d/conf.yaml
ADD redisdb.yaml /etc/datadog-agent/conf.d/redisdb.d/conf.yaml
ADD postgres.yaml /etc/datadog-agent/conf.d/postgres.d/conf.yaml
ADD docker_logs.yaml /etc/datadog-agent/conf.d/docker_logs.d/conf.yaml
