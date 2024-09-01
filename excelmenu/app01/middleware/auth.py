import time
import hashlib
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class allow_ip_middleware(MiddlewareMixin):
    def process_request(self, request):
        can_ip=['b8aed072d29403ece56ae9641638ddd50d420f950bde0eefc092ee8879554141','d6375d91abb8048a03da5e018e40c1b0eb306b7525d0dbf6ba5dc031b4b4646d','be2b775cb8cd43b8c85763d3c635f7ad4b208a6dac6755f6b734971475e2f083','6ea9726cad599cc417f0fe20823a73df56c922384cae3ba69adc1ebf433a84d3']
        ip_address = request.META.get('REMOTE_ADDR')
        hash_list=self.sha256_encode(ip_address)
        flag=False
        for ip_duan in hash_list:
            if ip_duan in can_ip:
                flag=True
        if not flag:
            return redirect('http://www.baidu.com')

    def process_response(self, request, response):
        return response

    def sha256_encode(self,ip_address):
        ip_1='.'.join(ip_address.split('.')[0:1])
        ip_2='.'.join(ip_address.split('.')[0:2])
        hash_list=[]
        sha256 = hashlib.sha256()
        sha256.update(ip_1.encode('utf-8'))
        hash_list.append(sha256.hexdigest())

        sha256 = hashlib.sha256()
        sha256.update(ip_2.encode('utf-8'))
        hash_list.append(sha256.hexdigest())
        return hash_list
class write_ip(MiddlewareMixin):
    def process_request(self, request):
        if request.path=='/':
            ip_address = request.META.get('REMOTE_ADDR')
            current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            data=f'访问时间{current_time} ip地址{ip_address}\n'
            with open('./app01/static/txt/ip.txt', "a", encoding='utf-8') as fp:
                fp.write(data)
    def process_response(self, request, response):
        return response
