import json
from haproxystats import HAProxyServer

def get_lb_stats():
    haproxy = HAProxyServer('127.0.0.1:80')
    print(haproxy.to_json())

get_lb_stats()
