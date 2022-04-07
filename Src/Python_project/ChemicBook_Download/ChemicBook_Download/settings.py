# Scrapy settings for ChemicBook_Download project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ChemicBook_Download'

SPIDER_MODULES = ['ChemicBook_Download.spiders']
NEWSPIDER_MODULE = 'ChemicBook_Download.spiders'

# 设置日志
LOG_LEVEL = "WARNING"
LOG_FILE = "ChemicBook.log"

PROXIES = [
    'http://120.24.76.81:8123',
    'http://58.215.201.98:56566',
]

# PROXY_LIST = [
#     # 这个后面可以加收费的，输入账号密码
#     # {"ip_port":"152.136.62.181:9999","user_passwd":"****"},
#     {"ip_port": "117.114.149.66:55443"},
#     {"ip_port": "202.55.5.209:8090"},
#     {"ip_port": "152.136.62.181:9999"},
#     {"ip_port": "120.220.220.95:8085"},
#     {"ip_port": "120.220.220.95:8085"},
#     {"ip_port": "223.96.90.216:8085"},
#     {"ip_port": "47.113.90.161:83"},
#     {"ip_port": "47.92.234.75:80"},
#     {"ip_port": "202.55.5.209:8090"},
#     {"ip_port": "47.92.234.75:80"},
#     {"ip_port": "202.55.5.209:8090"},
#     {"ip_port": "202.55.5.209:8090"},
# ]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ChemicBook_Download (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 把并发改小一点
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
   # 'ChemicBook_Download.middlewares.ChemicbookDownloadSpiderMiddleware': 543,
   #  'ChemicBook_Download.middlewares.RandomProxyMiddleware': 745,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# 注册代理组件
# DOWNLOADER_MIDDLEWARES = {
    # 'ChemicBook_Download.middlewares.ChemicbookDownloadDownloaderMiddleware': 543,
    # 具体查看这个 https://blog.csdn.net/a__int__/article/details/104748788?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_aa&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_aa&utm_relevant_index=5
    #这个是免费的代理组件
    # 'ChemicBook_Download.middlewares.RandomProxyMiddleware': 100,
    # 下面这个是收费的代理组件
    # 'ChemicBook_Download.middlewares.AbuyunProxyMiddleware': 101,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'ChemicBook_Download.pipelines.ChemicbookDownloadPipeline': 300,
    # 'ChemicBook_Download.pipelines.ChemicbookDownloadGifPipeline': 290,
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
