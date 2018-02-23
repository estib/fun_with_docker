from datadog import initialize, api
import os

options = {
    'api_key': os.environ['API_KEY'],
    'app_key': os.environ['APP_KEY']
}

initialize(**options)

mysql_title = "MySQL Demo Test"

mysql_description = "Prototype for MySQL Docker"

mysql_graphs = [{"definition": { "events": [], "requests": [{"q": "avg:mysql.net.connections{*}"}], "viz": "timeseries"}, "title": "Average MySQL Net Connections"},
                {"definition": { "events": [], "requests": [{"q": "avg:mysql.performance.queries{*}"}], "viz": "timeseries"}, "title": "Average MySQL Performance Queries"},
                {"definition": { "events": [], "requests": [{"q": "avg:mysql.net.max_connections{*}", "type":"area"}], "viz": "timeseries"}, "title": "Average MySQL Max Connections"}
                ]

template_variables = [{
    "name": "host1",
    "prefix": "host",
    "default": "host:my-host"
}]


read_only = True
api.Timeboard.create(title=mysql_title, description=mysql_description, graphs=mysql_graphs, template_variables=template_variables, read_only=read_only)


redis_title = "Redis Demo Test"

redis_description = "Prototype for Redis Docker"

redis_graphs = [{"definition": { "events": [], "requests": [{"q": "avg:redis.cpu.sys{*}"}], "viz": "timeseries"}, "title": "Average Redis CPU System Performance"},
                {"definition": { "events": [], "requests": [{"q": "avg:redis.net.clients{*}"}], "viz": "timeseries"}, "title": "Average Redis Net Clients"},
                {"definition": { "events": [], "requests": [{"q": "avg:redis.aof.rewrite{*}", "type":"area"}], "viz": "timeseries"}, "title": "Average Redis AOF Rewrites"}
                ]



api.Timeboard.create(title=redis_title, description=redis_description, graphs=redis_graphs, template_variables=template_variables, read_only=read_only)

es_title = "Elasticsearch Demo Test"

es_description = "Prototype for ES Docker"

es_graphs = [{"definition": { "events": [], "requests": [{"q": "avg:elasticsearch.docs.count{*}"}], "viz": "timeseries"}, "title": "Average ES Document Counts"},
             {"definition": { "events": [], "requests": [{"q": "avg:elasticsearch.store.size{*}"}], "viz": "timeseries"}, "title": "Average ES Store Size"}
            ]



api.Timeboard.create(title=es_title, description=es_description, graphs=es_graphs, template_variables=template_variables, read_only=read_only)




pg_title = "Postgres Demo Test"

pg_description = "Prototype for PG Docker"

pg_graphs = [{"definition": { "events": [], "requests": [{"q": "avg:postgresql.bgwriter.checkpoints_timed{*}"}], "viz": "timeseries"}, "title": "Average PG timed checkpoints"},
             {"definition": { "events": [], "requests": [{"q": "avg:postgresql.max_connections{*}"}], "viz": "timeseries"}, "title": "Average PG Max Connections"}
            ]


api.Timeboard.create(title=pg_title, description=pg_description, graphs=pg_graphs, template_variables=template_variables, read_only=read_only)

