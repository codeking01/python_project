# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import time
from random import random

from scrapy import signals
# from Pubchemic_download.settings import PROXY_LIST

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class PubchemicDownloadSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class PubchemicDownloadDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



# 定义一个中间类 随机头和ip都可以
# class RandomProxy(object):
#     def process_request(self, request, spider):
#         proxy = random.choice(PROXY_LIST)
#         print(proxy)
#         if 'user_passwd' in proxy:
#             # 对账号密码进行编码
#             b64_up = base64.base64.b64encode(proxy['user_passwd'].encode())
#             # 设置认证
#             request.headers['Proxy-Authorization'] = 'Basic ' + b64_up.decode()
#             # 设置代理
#             request.meta['proxy'] = proxy['ip_port']
#             pass
#         else:
#             # 设置代理
#             request.meta['proxy'] = proxy['ip_port']



# 增加一个加代理的类 一会在setting中打开
# class ProxyMiddleWare(object):
#     """docstring for ProxyMiddleWare"""
#     def process_request(self, request, spider):
#         '''对request对象加上proxy'''
#         proxy = self.get_random_proxy()
#         print("this is request ip:" + proxy)
#         request.meta['proxy'] = proxy
#
#     def process_response(self, request, response, spider):
#         '''对返回的response处理'''
#         #如果返回的response状态不是200,重新生成当前request对象
#         if response.status != 200:
#             proxy = self.get_random_proxy()
#             print("this is response ip:" + proxy)
#             # 对当前request加上代理
#             request.meta['proxy'] = proxy
#             return request
#         return response
#
#     def get_random_proxy(self):
#         '''随机从文件中读取proxy'''
#         while 1:
#             with open('D:/Task_Datas/proxies.txt', 'r') as f:
#                 proxies = f.readlines()
#             if proxies:
#                 break;
#             else:
#                 time.sleep(1)
#         proxy = random.choice(proxies).strip()
#         return proxy
