"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/5/12 16:38
    @File : Nist_Properties.py
"""
import requests
from lxml import etree
from openpyxl import load_workbook
from tqdm import tqdm


# 根据传来的字典秀娥如到excel里面
def save_to_excel(cas, current_index, table, content_dict):
    for key in content_dict:
        the_values = content_dict.get(key)
        # print(the_values)
        table.cell(current_index + 1, 1, cas)
        table.cell(current_index + 1, 2, str(key))
        table.cell(current_index + 1, 3, str(the_values))


def GetCasList(rows):
    casList = []
    for sheet_row in tqdm(range(rows + 1)):
        cas = sheet.cell(row=sheet_row + 2, column=2).value
        if (cas != None):
            casList.append(cas)
    return casList


if __name__ == '__main__':
    # 存储的excel文件
    save_path = 'Nist_Properties.xlsx'
    data = load_workbook(save_path)
    sheetnames = data.sheetnames
    # 获取第一张表
    table = data[sheetnames[0]]
    #  读取excel的cas号
    read_path = 'test.xlsx'
    wb = load_workbook(read_path)
    sheet = wb['Sheet1']
    # 读取excel中的最大行数
    rows = sheet.max_row
    allcas_list = GetCasList(rows)
    current_index = 0
    # 挨个 遍历
    for index in tqdm(range(rows)):
        cas = allcas_list[index]
        url = 'https://webbook.nist.gov/cgi/cbook.cgi?ID={cas}&Units=SI'.format(cas=cas)
        response = requests.get(url)
        res_content = response.text
        # next_url = tree.xpath(r'''//a[contains(text(),'NIST / TRC Web Thermo Tables, professional edition')]/@href''')
        # 看看是否有链接存在
        content_flag = 'Data at NIST subscription sites'

        # 判断有链接才接着往下走
        if (content_flag in res_content):
            try:
                tree = etree.HTML(res_content)
                next_url = tree.xpath(r'//*[@id="main"]/ul[2]/li/a/@href')
                next_url = next_url[0]
                # 处理数据
                next_content = requests.get(next_url).text
                next_tree = etree.HTML(next_content)
                i = 1
                # 获取所有的性质
                while (True):
                    # 用来存储性质内容的字典
                    content_dict = {}
                    eachproperty = next_tree.xpath(f'//div/ul/li[{i}]/text()')
                    if (len(eachproperty) == 0):
                        # 出现了空列表就结束循环
                        break
                    # 先判断是不是多标题的
                    eachproperties = next_tree.xpath(f'//div/ul/li[{i}]//li//text()')
                    if (len(eachproperties) == 0):
                        # 处理单标题
                        signal_propety = next_tree.xpath(f'//div/ul/li[{i}]//text()')
                        content_dict.update({str(signal_propety[0].strip()): str(signal_propety[1].strip())})
                    else:
                        # 存储多标题的
                        propetyname = next_tree.xpath(f'//div/ul/li[{i}]//text()')[0].strip()
                        eachproperties = [str(temp).strip() for temp in eachproperties]
                        propetyvalue = eachproperties
                        content_dict.update({str(propetyname): propetyvalue})
                    # 存储到excel中
                    cas = cas.replace('-', '_')
                    save_to_excel(cas, current_index, table, content_dict)
                    data.save(save_path)
                    current_index += 1
                    i += 1
                # print(f'第{index}个数据处理结束！cas号为{cas}')
            except Exception as e:
                print(f'未知错误: {e}')
                print(f'原始url: {url},最终url:{next_url}')
                current_index += 1
                data.save(save_path)
        # 如果没有链接，则写入提示数据到excel里面
        else:
            cas = cas.replace('-', '_')
            # 只写cas号即可
            table.cell(current_index + 1, 1, cas)
            table.cell(current_index + 1, 2, '没有数据！')
            print(f'数据不存在，当前cas为{cas},链接为{url}')
            data.save(save_path)
            current_index += 1
