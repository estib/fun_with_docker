from datadog import initialize, api
import os

options = {
    'api_key': os.environ['API_KEY'],
    'app_key': os.environ['APP_KEY']
}

initialize(**options)

title = "Redis Demo Test"

description = "Prototype for Redis Docker"

graphs = [{"definition": { "events": [], "requests": [{"q": "avg:redis.cpu.sys{*}"}], "viz": "timeseries"}, "title": "Average Redis CPU System Performance"},
          {"definition": { "events": [], "requests": [{"q": "avg:redis.net.clients{*}"}], "viz": "timeseries"}, "title": "Average Redis Net Clients"},
          {"definition": { "events": [], "requests": [{"q": "avg:redis.aof.rewrite{*}", "type":"area"}], "viz": "timeseries"}, "title": "Average Redis AOF Rewrites"}
          ]

template_variables = [{
    "name": "host1",
    "prefix": "host",
    "default": "host:my-host"
}]


read_only = True
api.Timeboard.create(title=title, description=description, graphs=graphs, template_variables=template_variables, read_only=read_only)
