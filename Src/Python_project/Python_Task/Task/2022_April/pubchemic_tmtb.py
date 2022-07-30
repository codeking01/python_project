# -- coding: utf-8 --
# @Time : 2022/4/10 11:45
# @Author : codeking
# @File : pubchemic_tmtb.py
import json
import requests
from fake_useragent import UserAgent
from lxml import etree


def IS_Right(func):
    def wrapper(*args):
        flag = func(*args)
        if (flag != "NULL"):
            obj_cid = str(flag)
            return obj_cid
        else:
            return "erro"

    return wrapper


@IS_Right
def get_cid(deal_cas):
    try:
        # 下面这个是为了获取需要链接的cid号
        url = 'https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi?infmt=json&outfmt=json&query={%22select%22:%22*%22,%22collection%22:%22compound%22,%22where%22:{%22ands%22:[{%22cid%22:%22' + str(
            deal_cas) + '%22}]},%22order%22:[%22cid,asc%22],%22start%22:1,%22limit%22:10,%22width%22:1000000,%22listids%22:0}'
        response = requests.get(url=url, headers=headers)
        response.encoding = 'utf-8'
        # 下面这个json数据可以采集到
        json_content = response.text
        # print(page_content)
        # ***可以直接读取json，就不存进去了
        obj = json.loads(json_content)
        # 找到json中相应的数据
        obj_cid = obj["SDQOutputSet"][0]["rows"][0]["cid"]
        return obj_cid
    except:
        return "NULL"


# 获取json的内容
def get_jsoncontent(obj_cid):
    json_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{obj_cid}/JSON/'.format(obj_cid=obj_cid)
    response = requests.get(url=json_url, headers=headers, timeout=220)
    response.encoding = 'utf-8'
    obj = json.loads(response.text)
    return obj


if __name__ == '__main__':
    headers = {'user-agent': UserAgent().Chrome}
    deal_cas = '57-27-2'
    obj_cid = get_cid(deal_cas)
    if (obj_cid == "erro"):
        print('cid号不存在')
        # todo  break 跳出循环
    else:
        # 获取熔点沸点
        obj = get_jsoncontent(obj_cid)
        pre_content = obj['Record']['Section']
        for item in pre_content:
            if (item['TOCHeading'] == 'Chemical and Physical Properties'):
                property = item['Section']
                for Pre_Tbf in property:
                    if (Pre_Tbf['TOCHeading'] == 'Experimental Properties'):
                        # 找到熔沸点
                        tbf_content=Pre_Tbf['Section']
                        for tb in tbf_content:
                            if (tb['TOCHeading'] == 'Boiling Point'):
                                # 找到沸点
                                tb_content=tb
                break


