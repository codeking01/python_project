import time
import urllib
import urllib.request

import winsound
from lxml import etree
import requests
from Deal_Excel.Basic_Excle import DoExcel

if __name__ == '__main__':
    # 先从excel里面取出cas 先读取mol的
    excel_data = DoExcel(
        read_path='/src.code/code/mol失败的cas汇总.xlsx',
        sheet_name='cas')
    excel_content = excel_data.Read_Data()
    # 获取所有cas号的列表
    cas_list = excel_content.cas_list
    deal_cas_list = excel_content.deal_cas_list
    for i in range(len(deal_cas_list)):
        deal_cas_list[i] = deal_cas_list[i].replace('-', '_')
    # mol_url=' https://www.chemicalbook.com/CAS/MOL/{mol_url}.mol'.format(mol_url=deal_cas)
    # gif_url='https://www.chemicalbook.com/CAS/GIF/{png_url}.gif'.format(png_url=deal_cas)
    # 处理 mol下载失败的数据
    k=0
    for i in range(10117,len(deal_cas_list)):
        # try:
        #     mol_url = 'https://www.chemicalbook.com/CAS/MOL/{mol_url}.mol'.format(mol_url=cas_list[i])
        #     urllib.request.urlretrieve(mol_url, 'D:/Task_Datas/scrapy_mol/' + str(deal_cas_list[i]) + '.mol')
        #     print('第{current_num}条数据的mol文件处理成功'.format(current_num=i))
        #
        # except:
            try:
                new_url = 'https://www.chemicalbook.com/Search.aspx?_s=&keyword={cas}'.format(cas=str(cas_list[i]))
                response = requests.get(new_url)
                tree = etree.HTML(response.text)
                base_url = tree.xpath('//a[normalize-space()="Mol"]/@href')[0]
                new_mol_url = 'https://www.chemicalbook.com/{base_url}'.format(base_url=base_url)
                urllib.request.urlretrieve(new_mol_url, 'D:/Task_Datas/ChemicBookMol/' + str(deal_cas_list[i]) + '.mol')
                print('第{current_num}条数据的mol文件处理成功'.format(current_num=i))
                k=0
            except Exception as e :
                k+=1
                # 记录失败的cas
                with open("mol_fails.txt", encoding='utf-8', mode='a+') as f:
                    f.write("第{current_num}条数据的mol文件处理失败,cas号可能有问题:{cas}".format(current_num=i, cas=deal_cas_list[i]))
                    # 报警10s
                if(k>10):
                    # winsound.Beep(500, 50000)
                    # time.sleep(5)
                    k=0
                print('第{i}条数据失败,失败原因{e},cas号为:{cas}，链接为: {mol_url}'.format(i=i, e=e, cas=deal_cas_list[i],mol_url=new_url))
