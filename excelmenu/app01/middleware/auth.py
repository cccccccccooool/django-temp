import time
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class allow_ip_middleware(MiddlewareMixin):
    def process_request(self, request):
        can_ip=['127.0.0.1','183.9.65.99','120.87.218.47']
        ip_address = request.META.get('REMOTE_ADDR')
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        data=f'访问时间{current_time} ip地址{ip_address}\n'
        with open('./app01/static/txt/ip.txt', "a", encoding='utf-8') as fp:
            fp.write(data)
        if ip_address not in can_ip:
            return redirect('http://www.baidu.com')


    def process_response(self, request, response):
        return response