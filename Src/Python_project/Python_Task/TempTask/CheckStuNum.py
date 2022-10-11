# auth: code_king
# time: 2022/8/29 8:49
# file: CheckStuNum.py
import re
import os

'''
检查没提交材料的同学的学号
'''

if __name__ == '__main__':
    # path定义要获取的文件名称的目录
    path = "C:/Users/king/Documents/WeChat Files/wxid_r24hlo4eeq7c22/FileStorage/File/2022-08"
    # os.listdir()方法获取文件夹名字，返回数组
    file_name_list = os.listdir(path)
    # 转为转为字符串
    file_name = str(file_name_list)
    # 定义正则
    Num_pattern = re.compile(r"(\d{2,8})")
    Nums = Num_pattern.findall(file_name)
    # 取出学号的后两位
    Nums_List = [x[-2:] for x in Nums]
    # 将列表的值转成int
    Nums_List = list(map(int, Nums_List))
    tempList = [29, 23, 4, 8, 26, 27, 40, 31, 32, 1, 13, 7, 16, 15, 39]
    for i in tempList:
        Nums_List.append(i)
    # 新建学号列表
    full_stu_num = range(1, 41)
    new_list = [item for item in full_stu_num if item not in Nums_List]
    print(new_list)
