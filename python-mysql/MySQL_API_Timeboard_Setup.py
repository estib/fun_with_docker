from datadog import initialize, api
import os

options = {
    'api_key': os.environ['API_KEY'],
    'app_key': os.environ['APP_KEY']
}

initialize(**options)

title = "MySQL Demo Test"

description = "Prototype for MySQL Docker"

graphs = [{"definition": { "events": [], "requests": [{"q": "avg:mysql.net.connections{*}"}], "viz": "timeseries"}, "title": "Average MySQL Net Connections"},
          {"definition": { "events": [], "requests": [{"q": "avg:mysql.performance.queries{*}"}], "viz": "timeseries"}, "title": "Average MySQL Performance Queries"},
          {"definition": { "events": [], "requests": [{"q": "avg:mysql.net.max_connections{*}", "type":"area"}], "viz": "timeseries"}, "title": "Average MySQL Max Connections"}
          ]

template_variables = [{
    "name": "host1",
    "prefix": "host",
    "default": "host:my-host"
}]


read_only = True
api.Timeboard.create(title=title, description=description, graphs=graphs, template_variables=template_variables, read_only=read_only)
