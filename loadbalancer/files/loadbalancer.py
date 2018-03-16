#!/usr/bin/python
import json
from haproxystats import HAProxyServer

def get_lb_stats():
    haproxy = HAProxyServer('127.0.0.1:5000')
    print(haproxy.to_json())

get_lb_stats()
