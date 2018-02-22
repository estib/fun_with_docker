CREATE USER 'datadog'@'172.%' IDENTIFIED BY 'ddpass';
GRANT REPLICATION CLIENT ON *.* TO 'datadog'@'172.%' WITH MAX_USER_CONNECTIONS 5;
GRANT PROCESS ON *.* TO 'datadog'@'172.%';
GRANT SELECT ON performance_schema.* TO 'datadog'@'172.%';
