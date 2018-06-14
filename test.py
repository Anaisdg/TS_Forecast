from influxdb import InfluxDBClient
from json_to_line_test import json_body2
import pandas as pd

json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "value": 0.64
        }
    }
]


client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example2')

client.create_database('example2')

client.write_points(json_body2)

result = client.query('select value from cpu_load_short;')

print("Result: {0}".format(result))
