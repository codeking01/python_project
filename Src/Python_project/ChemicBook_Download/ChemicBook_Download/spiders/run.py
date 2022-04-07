from scrapy import cmdline
# 作为主程序入口 代替终端的 scrapy crawl 名字
cmdline.execute('scrapy crawl chemicbook'.split())

# 这个是main函数也是整个程序入口的惯用写法
# if __name__ == '__main__':
#     execute(['scrapy', 'crawl', 'httpbin'])