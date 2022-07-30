#-*-coding:utf-8-*-
import requests
from lxml import etree
import random
import time
import json
url='https://www.hao123.com/?tn=57028281_7_hao_pg'
proxyaddr = "27.188.197.81"    #代理IP地址
proxyport = 57114              #代理IP端口
proxyusernm = "17746532048"        #代理帐号
proxypasswd = "fxjie1998"        #代理密码
#name = input();
proxyurl="http://"+proxyusernm+":"+proxypasswd+"@"+proxyaddr+":"+"%d"%proxyport

t1 = time.time()
r = requests.get(url,proxies={'http':'27.188.197.81:57114'},headers={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cache-Control":"max-age=0",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"})
r.encoding='gb2312'

t2 = time.time()

print(r.text)
print("时间差:" , (t2 - t1))

# start=time.time()
# proxies_pool = [
#     {'http': '119.102.98.89:57114'},
#     {'http':'114.239.198.244:57114' },
#     {'http':'27.188.197.81:57114' },
#     {'http':'119.36.14.88:57114' },
#     {'http':'180.116.211.246:57114' }
# ]
# for i in proxies_pool:
#     proxies=i
#     url='https://webbook.nist.gov/cgi/cbook.cgi?ID=C64175&Units=SI&Mask=4#Thermo-Phase'
#     page_text = requests.get(url, proxies=proxies)
#     end=time.time()
#     print(proxies,page_text,end-start)

