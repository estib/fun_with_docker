CREATE USER 'ubuntu'@'172.%' IDENTIFIED BY 'ubuntupass';
GRANT ALL ON world.* TO 'ubuntu'@'172.%' WITH MAX_USER_CONNECTIONS 5;
