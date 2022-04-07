# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import random
from collections import defaultdict

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.exceptions import NotConfigured

from Python_project.ChemicBook_Download.ChemicBook_Download import settings


class ChemicbookDownloadSpiderMiddleware:
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


class ChemicbookDownloadDownloaderMiddleware:
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


# 添加自己定义的代理中间件
# 这个是定义的 免费的 代理
# class RandomProxyMiddleware(object):
#     PROXIES = [
#         'http://120.24.76.81:8123',
#         'http://58.215.201.98:56566',
#     ]
#     def process_request(self, request, spider):
#         # 随机从其中选择一个，并去除左右两边空格
#         proxy = random.choice(self.PROXIES).strip()
#         # 打印结果出来观察
#         print("this is request ip:" + proxy)
#         # 设置request的proxy属性的内容为代理ip
#         request.meta['proxy'] = proxy
#     def process_response(self, request, response, spider):
#         if (response.status != 200):
#             my_proxy = random.choice(self.PROXIES).strip()
#             print('当前的代理ip为:', my_proxy)
#             request.meta['proxy'] = my_proxy
#             return request
#         return response


# 定义收费的代理 的开启组件
# class AbuyunProxyMiddleware(object):
#     #代理服务器
#     proxy_Server="http://https://www.abuyun.com/"
#     # 隧道信息
#     proxy_User=''
#     proxy_Pass=''
#     encode_user_pass=proxy_User+':'+proxy_Pass
#     proxyAuth='Basic'+base64.urlsafe_b64encode(encode_user_pass.encode()).decode()
#     def process_request(self, request, spider):
#         request.meta['proxy'] = self.proxy_Server
#         # 配置认证信息
#         request.headers['proxy-Authorization'] =self.proxyAuth
#
#     def process_response(self, request, response, spider):
#         if (response.status != 200):
#             my_proxy = random.choice(self.PROXIES).strip()
#             print('当前的代理ip为:', my_proxy)
#             request.meta['proxy'] = my_proxy
#             request.headers['Proxy-Authorization'] =self.proxyAuth
#             return request
#         return response

# class RandomProxyMiddleware(object):
#     def __int__(self, settings):
#         # 2、初始化配置及相关变量
#
#         # proxies读取代理ip
#         self.proxies = settings.getlist('PROXIES')
#         self.stats = defaultdict(int)
#         self.max_failed = 3
#
#     # classmethod 修饰符对应的函数不需要实例化，不需要 self 参数
#     # 但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性\方法\实例化对象等。
#     # 不使用classmethod，不传递传递默认self参数的方法（该方法也是可以直接被类调用的，但是这样做不标准）
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # 1、创建中间件对象
#
#         # 判断如果没有启用代理
#         if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
#             # 返回异常
#             raise NotConfigured
#         return cls(crawler.settings)
#
#     def process_request(self, request, spider):
#         # 3、为每个request对象分配一个随机IP代理
#
#         # 如果spider里面没有proxy才赋值
#         if not request.meta.get('proxy') and request.url not in spider.start_urls:
#             proxy = random.choice(self.proxies)
#             request.meta['proxy'] =proxy
#             print('当前ip为:',proxy)
#             # request.meta['proxy'] = random.choice(self.proxies)
#
#     def process_response(self, request, response, spider):
#         # 4、请求成功则调用
#
#         c = request.meta.get("proxy")
#         if response.status in (400, 401, 403):
#             self.stats[c] += 1
#         if self.stats[c] >= self.max_failed:
#             print("报错")
#             if c in self.proxies:
#                 self.proxies.remove(c)
#                 print("已从列表里删除%s" % c)
#             del request.meta["proxy"]
#             return request
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # 4、请求失败则调用
#
#         c = request.meta.get("proxy")
#         from twisted.internet.error import ConnectionRefusedError, TimeoutError
#         if c and isinstance(exception, (ConnectionRefusedError, TimeoutError)):
#             print("执行代理%s发现错误：%s" % (c, exception))
#             if c in self.proxies:
#                 self.proxies.remove(c)
#                 print("已从列表里删除%s" % c)
#             del request.meta["proxy"]
#             return request


# 定义一个中间类 随机头和ip都可以
# class RandomProxy(object):
#
#     def process_request(self, request, spider):
#         proxy = random.choice(PROXY_LIST)
#         print(proxy)
#         if 'user_passwd' in proxy:
#             # 对账号密码进行编码
#             b64_up = base64.b64encode(proxy['user_passwd'].encode())
#             # 设置认证
#             request.headers['Proxy-Authorization'] = 'Basic ' + b64_up.decode()
#             # 设置代理
#             request.meta['proxy'] = proxy['ip_port']
#             pass
#         else:
#             print("当前的ip为",proxy['ip_port'])
#             # 设置代理
#             request.meta['proxy'] = proxy['ip_port']
