# -*- coding=utf-8 -*-
import random
# import base64
class ProxyMiddleware(object):
    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        ip = random.choice(self.ip_list)
        print(ip)
        request.meta['proxy'] = ip

    ip_list =[
            'https://218.29.111.106:9999',
            'https://119.23.129.24:3128',]
