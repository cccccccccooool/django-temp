import time
import hashlib
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class allow_ip_middleware(MiddlewareMixin):
    def process_request(self, request):
        can_ip=['5909dbb7f903a6bcffec3a05a1d5f33b275659feaddc55831a16ebd1a90e92b5','da135c4a34b29c4db77f062e2da21e4a514eb5d50034e6c96beb21e0751ca4d6','0f03a4c577b5754def4855be3c3f5a420c2c80daba4ec64c799a4a57a75727eb','d6375d91abb8048a03da5e018e40c1b0eb306b7525d0dbf6ba5dc031b4b4646d','be2b775cb8cd43b8c85763d3c635f7ad4b208a6dac6755f6b734971475e2f083']
        ip_address = request.META.get('REMOTE_ADDR')
        ip_a='.'.join(ip_address.split('.')[0:2])
        sha256 = hashlib.sha256()
        sha256.update(ip_a.encode('utf-8'))
        hash_value = sha256.hexdigest()
        if hash_value not in can_ip:
            return redirect('http://www.baidu.com')

    def process_response(self, request, response):
        return response

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