import requests
from fake_useragent import UserAgent
from lxml import etree

headers = {'user-agent': UserAgent().Chrome}

if __name__ == '__main__':
    # page [0,367)
    for pagenum in range(0, 367):
        #这个是爬取的页码
        # 起始地址
        # https://www.chemicalbook.com/ProductCASList_12_0_EN.htm
        url = 'https://www.chemicalbook.com/ProductCASList_15_{page}00_EN.htm'.format(page=pagenum)
        # cas号
        # //tr[n-1]/td[3]/a
        # MF号
        # //*[@id="ContentPlaceHolder1_ProductClassDetail_MF_n"]/text()
        response = requests.get(url=url, headers=headers, proxies=None)
        tree = etree.HTML(response.text)
        # 解析cas号
        all_cas=tree.xpath('//td[3]/a/text()')
        all_mf=tree.xpath('//td[4]/span/text()')
        print('cas',all_cas)
        print('mf',all_mf)
