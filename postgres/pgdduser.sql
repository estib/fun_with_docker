CREATE USER datadog WITH password 'dbpass';
GRANT SELECT ON pg_stat_database TO datadog;