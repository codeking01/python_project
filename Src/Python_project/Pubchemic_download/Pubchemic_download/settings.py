# Scrapy settings for Pubchemic_download project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Pubchemic_download'

SPIDER_MODULES = ['Pubchemic_download.spiders']
NEWSPIDER_MODULE = 'Pubchemic_download.spiders'

# PROXY_LIST =[
#     #这个后面可以加收费的，输入账号密码
#     # {"ip_port":"152.136.62.181:9999","user_passwd":"****"},
#     {"ip_port":"152.136.62.181:9999"},
# ]

# 设置日志
# LOG_LEVEL= ""
LOG_FILE = "Pubchem.log"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 打开UA
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.20 Safari/537.36'

# Obey robots.txt rules
# 关闭君子协议
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#  CONCURRENT_REQUESTS：最大并发数，很好理解，就是同时允许开启多少个爬虫线程
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED：是否保存COOKIES，默认关闭，开机可以记录爬取过程中的COKIE，非常好用的一个参数
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS :默认请求头，上面写了一个USER_AGENT，其实这个东西就是放在请求头里面的，这个东西可以根据你爬取的内容做相应设置。
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# 添加代理
# SPIDER_MIDDLEWARES = {
#    # 'Pubchemic_download.middlewares.PubchemicDownloadSpiderMiddleware': 543,
#    'Pubchemic_download.middlewares.RandomProxy': 543,
# }

# 看着别的加的
# DOWNLOADER_MIDDLEWARES = {
#     # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':None,
#     'Pubchemic_download.middlewares.ProxyMiddleWare':125,
#     'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':None
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'Pubchemic_download.middlewares.PubchemicDownloadDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES：项目管道，300为优先级，越低越爬取的优先度越高
ITEM_PIPELINES = {
    'Pubchemic_download.pipelines.PubchemicDownloadPipeline': 300,
    'Pubchemic_download.pipelines.PubchemicDownloadpngPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
