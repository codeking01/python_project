import requests
from fake_useragent import UserAgent
from lxml import etree

headers = {'user-agent': UserAgent().Chrome}


#  todo 使用多态去实现其他的链接的下载
# 获取xpath解析的数据
class GetContent:
    def __init__(self, url=None, xpath_content=None):
        '''
        :param url: 传入需要解析的url
        :param xpath_content:  需要传入一个字典示例如下 {'需要获取的字段':'xpath语法'}
        '''
        self.url = url
        self.xpath_content = xpath_content

    # 用来获取xpath的解析内容
    # todo 当解析不出来的时候抛出指定的返回值
    def GetXpathContent(self):
        '''
        :return:  把解析好的内容打包成字典返回
        '''
        # 获取响应
        # todo 默认没有加代理，后续再去实现
        response = requests.get(self.url, headers=headers, proxies=None)
        tree = etree.HTML(response.text)
        # 通过传进来的xpath_content的列表 进行便利，依次获取需要的数据
        # todo  处理多个数据 可以用字典存储
        # 获取字典的所有键名
        xpath_content_key = []
        for i in self.xpath_content:
            xpath_content_key.append(i)
        # 获取所有解析的数据
        try:
            for content_key in xpath_content_key:
                try:
                    # 根据value去解析
                    self.xpath_content[content_key] = tree.xpath(self.xpath_content[content_key])[0]
                except:
                    # 如果解析失败
                    print("{item}字段的xpath语法有问题，或者xpath无法解析该字段\n".format(item=content_key))
        except Exception as e:
            print('Unexpected exception:', e)
        finally:
            # 把解析的内容打包成字典返回
            return self.xpath_content


# todo 下载图片
def Save_Pic(pic_url=None, path='.', cas=None, form=None,proxies=None):
    # todo 后面可以考虑加代理
    response = requests.get(url=pic_url,proxies=proxies)
    img = response.content
    # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
    with open('{path}/{cas}.{form}'.format(path=path, cas=cas, form=form), 'wb') as f:
        f.write(img)

# # 示例
# xpath_content = {
#     'a': '....',
# }
# test_content = GetContent(url='https://www.chemicalbook.com/Search.aspx?_s=&keyword=100-02-8',
#                           xpath_content=xpath_content)
# content = test_content.GetXpathContent()
# print('解析出来的字典', content)

# 通过下载链接下载图片格式内容，并且指定存储位置;记录失败的cas号，指定存储地址
