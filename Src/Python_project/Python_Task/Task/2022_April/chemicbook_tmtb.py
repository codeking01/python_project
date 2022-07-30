# -- coding: utf-8 --
# @Time : 2022/4/10 11:45
# @Author : codeking
# @File : chemicbook_tmtb.py
import requests
from fake_useragent import UserAgent
from lxml import etree

if __name__ == '__main__':
    headers = {'user-agent': UserAgent().Chrome}
    url='https://pubchem.ncbi.nlm.nih.gov/#query=57-27-2'
    content=requests.get(url=url,headers=headers).text
    tree = etree.HTML(content)
    cid=tree.xpath('//div[2]/div/div[1]/div[2]/div[2]/div/span/a/span/span/text()')