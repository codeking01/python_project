# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib.request
import urllib
from itemadapter import ItemAdapter

class PubchemicDownloadPipeline:
    def process_item(self, item, spider):
        mol_url=item.get('mol_url')
        cas=item.get('cas')
        if (mol_url!="NULL"):
            current_num=item.get('current_num')
            urllib.request.urlretrieve(mol_url, 'D:/Task_Datas/scrapy_mol/' + str(cas) + '.sdf')
            print('第{current_num}条数据的mol文件处理成功'.format(current_num=current_num))
            return item
        else:
            pass

class PubchemicDownloadpngPipeline:
    def process_item(self, item, spider):
        png_url=item.get('png_url')
        cas=item.get('cas')
        if (png_url!="NULL"):
            current_num=item.get('current_num')
            urllib.request.urlretrieve(png_url, 'D:/Task_Datas/scrapy_png/' + str(cas) + '.png')
            print('第{current_num}条数据的png文件处理成功'.format(current_num=current_num))
            return item
        else:
            pass