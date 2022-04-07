import time
import urllib
import urllib.request

import winsound
from lxml import etree
import requests
from CodekingPython.Deal_Excel.Basic_Excle import DoExcel
from CodekingPython.Deal_contents.Do_Download import Save_Pic

if __name__ == '__main__':
    # 先从excel里面取出cas 先读取mol的
    excel_data = DoExcel(
        read_path='C:\All_Softwares\Develop_Tools\Idea_Project\CodekingPython\src.code\gif失败的cas汇总.xlsx',
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
    k = 0
    # todo 每150次换一次IP地址
    proxies = [
        # '202.55.5.209:8090',
        # '183.247.199.126:30001',
        # '202.55.5.209:8090',
        # '47.113.90.161	:83',
        '202.55.5.209	:8090',
        '117.95.100.230	:8089',
        '120.220.220.95	:8085',
        '106.55.15.244	:8889',
        '119.179.140.103:	8060',
        '220.168.52.245:53548',
    ]
    for i in range(10950, len(deal_cas_list)):
        # try:
        #     mol_url = 'https://www.chemicalbook.com/CAS/MOL/{mol_url}.mol'.format(mol_url=cas_list[i])
        #     urllib.request.urlretrieve(mol_url, 'D:/Task_Datas/scrapy_mol/' + str(deal_cas_list[i]) + '.mol')
        #     print('第{current_num}条数据的mol文件处理成功'.format(current_num=i))
        #
        # except:
        use_nums = 0
        index = 0
        try:
            # todo 加代理 150个换一次
            if (use_nums > 150):
                try:
                    index+=1
                    use_nums = 0
                except:
                    # ip不够了
                    winsound.Beep(500, 2000)
                    time.sleep(50)
                    print('换ip`````````')
            new_url = 'https://www.chemicalbook.com/Search.aspx?_s=&keyword={cas}'.format(cas=str(cas_list[i]))
            response = requests.get(new_url, proxies={'http': proxies[index].strip()})
            # ip_and_port = response.raw._connection.sock.getpeername()
            # print('IP代理:',ip_and_port)
            tree = etree.HTML(response.text)
            base_url = tree.xpath('//td[1]/img/@src')[0]
            new_gif_url = 'https://www.chemicalbook.com/{base_url}'.format(base_url=base_url)
            Save_Pic(pic_url=new_gif_url, path='D:/Task_Datas/ChemicBookGif/', cas=str(deal_cas_list[i]), form='gif',proxies={'http': proxies[index].strip()})
            # urllib.request.urlretrieve(new_gif_url, 'D:/Task_Datas/ChemicBookGif/' + str(deal_cas_list[i]) + '.gif')
            print('第{current_num}条数据的gif文件处理成功'.format(current_num=i))
            use_nums += 1
            k = 0
            # time.sleep(2)
        except Exception as e:
            use_nums += 1
            k += 1
            # 记录失败的cas
            with open("gif_fails.txt", encoding='utf-8', mode='a+') as f:
                f.write("第{current_num}条数据的gif文件处理失败,cas号可能有问题:{cas}".format(current_num=i, cas=deal_cas_list[i]))
                # 报警10s
            if (k > 10):
                winsound.Beep(500, 2000)
                # time.sleep(5)
                k = 0
            print(
                '第{i}条数据失败,失败原因{e},cas号为:{cas}，链接为: {gif_url}'.format(i=i, e=e, cas=deal_cas_list[i], gif_url=new_url))
