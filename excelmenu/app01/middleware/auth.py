import time
import hashlib
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class allow_ip_middleware(MiddlewareMixin):
    def process_request(self, request):
        can_ip=['12ca17b49af2289436f303e0166030a21e525d266e209267433801a8fd4071a0','5909dbb7f903a6bcffec3a05a1d5f33b275659feaddc55831a16ebd1a90e92b5','0f03a4c577b5754def4855be3c3f5a420c2c80daba4ec64c799a4a57a75727eb','1ed6bc1bf4ee69ba4e9225bdd72376010e26565bada0b5265161c08347a78fa0']
        ip_address = request.META.get('REMOTE_ADDR')
        sha256 = hashlib.sha256()
        sha256.update(ip_address.encode('utf-8'))
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