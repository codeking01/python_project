# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re
import time
import urllib
import urllib.request

import winsound
from lxml import etree


class FontColor:
    OKBULE = '\033[94m'
    OKGREEN = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[91m'


font_control = FontColor()

# 用来爬取mol的管道
from tqdm import tqdm

# 这个requests 必须导入
import requests


# mol的下载
class ChemicbookDownloadPipeline:
    def process_item(self, item, spider):
        # 获取下载的链接
        mol_url_list = item.get('mol_url_list')
        # 下面开始遍历下载的链接  第24999条数据的mol文件处理成功
        for i in tqdm(range(30000, len(mol_url_list))):
            final_mol_url = str(mol_url_list[i])
            # 通过正则取出这个cas号
            pattern = re.compile(r'.*MOL/(.*).mol')
            allgroup = pattern.search(final_mol_url)
            cas = allgroup[1]
            # 判断程序是不是挂掉了 count代表连续挂掉的次数
            count = 0
            try:
                urllib.request.urlretrieve(final_mol_url, 'D:/Task_Datas/scrapy_mol/' + str(cas) + '.mol')
                print('第{current_num}条数据的mol文件处理成功'.format(current_num=i))
                count = 0
            except:
                if (count < 15):
                    # xpath: //td[1]/div/a[1]/@href --> CAS/20210305/MOL/103582-45-2.mol
                    # 下载的mol的链接 https://www.chemicalbook.com/CAS/20210305/MOL/103582-45-2.mol
                    new_url = 'https://www.chemicalbook.com/Search.aspx?_s=&keyword={cas}'.format(cas=cas)
                    response = requests.get(new_url)
                    print(type(response.status_code), response.status_code)
                    # 判断一下状态码
                    if (response.status_code == 200):
                        try:
                            tree = etree.HTML(response.text)
                            base_url = tree.xpath('//td[1]/img/@src')[0]
                            new_mol_url = 'https://www.chemicalbook.com/{base_url}'.format(base_url=base_url)
                            urllib.request.urlretrieve(new_mol_url, 'D:/Task_Datas/scrapy_mol/' + str(cas) + '.mol')
                            print('第{current_num}条数据的mol文件处理成功'.format(current_num=i))
                        except:
                            with open("mol_fails.txt", "a+") as f:
                                f.write("第{current_num}条数据的mol文件处理失败,cas号可能有问题:{cas}".format(current_num=i, cas=cas))
                            count += 1
                            print(font_control.WARN + '第{current_num}条数据的mol文件处理失败,cas为：{cas}'.format(current_num=i,
                                                                                                      cas=cas))
                    else:
                        with open("mol_fails.txt", "a+") as f:
                            f.write('第{current_num}条数据的mol文件处理失败,{cas}号可能有问题,ip可能挂掉了\n'.format(current_num=i, cas=cas))
                        count += 1
                        print(
                            font_control.WARN + '第{current_num}条数据的mol文件处理失败,cas为：{cas}'.format(current_num=i, cas=cas),
                            '\n')
                        print(font_control.FAIL + 'ip不行了', '\n')
                else:
                    print(
                        font_control.FAIL + '程序挂掉了-----------------------------------------------------------------------')
                    # 报警10s
                    winsound.Beep(500, 10000)
                    time.sleep(60)
        return item


# 用来爬取gif的管道
class ChemicbookDownloadGifPipeline:
    def process_item(self, item, spider):
        # 获取下载的链接
        gif_url_list = item.get('gif_url_list')
        for i in tqdm(range(len(gif_url_list) - 1, len(gif_url_list)+1)):
            final_gif_url = str(gif_url_list[i])
            # 通过正则取出这个cas号
            pattern = re.compile(r'.*GIF/(.*).gif')
            allgroup = pattern.search(final_gif_url)
            cas = allgroup[1]
            count = 0
            try:
                urllib.request.urlretrieve(final_gif_url, 'D:/Task_Datas/scrapy_gif/' + str(cas) + '.gif')
                print('第{current_num}条数据的gif文件处理成功'.format(current_num=i))
                count = 0
            except:
                if (count < 15):
                    # 重新获取地址，地址有变 https://www.chemicalbook.com/Search.aspx?_s=&keyword=103582-45-2
                    new_url = 'https://www.chemicalbook.com/Search.aspx?_s=&keyword={cas}'.format(cas=cas)
                    # https://www.chemicalbook.com/CAS/20210305/GIF/103582-45-2.gif  CAS/20210305/GIF/103582-45-2.gif
                    response = requests.get(new_url)
                    print(type(response.status_code), response.status_code)
                    # 判断一下状态码
                    if (response.status_code == 200):
                        try:
                            tree = etree.HTML(response.text)
                            base_url = tree.xpath('//td[1]/img/@src')[0]
                            new_gif_url = 'https://www.chemicalbook.com/{base_url}'.format(base_url=base_url)
                            urllib.request.urlretrieve(new_gif_url, 'D:/Task_Datas/scrapy_mol/' + str(cas) + '.mol')
                            print('第{current_num}条数据的gif文件处理成功'.format(current_num=i))
                        except:
                            with open("gif_fails.txt", "a+") as f:
                                f.write("第{current_num}条数据的gif文件处理失败,cas号可能有问题:{cas}".format(current_num=i, cas=cas))
                            count += 1
                            print(font_control.WARN + '第{current_num}条数据的gif文件处理失败,数据可能不存在,cas为：{cas}'.format(
                                current_num=i, cas=cas), '\n')
                    else:
                        with open("gif_fails.txt", "a+") as f:
                            f.write('第{current_num}条数据的gif文件处理失败,cas号可能有问题:{cas}\n'.format(current_num=i, cas=cas))
                        count += 1
                        print(
                            font_control.WARN + '第{current_num}条数据的gif文件处理失败,cas为：{cas},ip可能挂掉了--'.format(current_num=i,
                                                                                                          cas=cas))

                        print(font_control.FAIL + 'ip不行了', '\n')
                else:
                    print(
                        font_control.FAIL + '程序挂掉了-----------------------------------------------------------------------',
                        '\n')
                    # 报警10s
                    winsound.Beep(500, 10000)
                    time.sleep(60)
        return item
