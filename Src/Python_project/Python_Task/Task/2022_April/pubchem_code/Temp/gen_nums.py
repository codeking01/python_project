'''
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/4/16 12:00
    @File : gen_nums.py
'''
# 这个用来生成序列数字，然后将其存入txt文件中
from tqdm import tqdm

if __name__ == '__main__':
    # 把1到1000 写入txt文件
    print('开始写入')
    for i in tqdm(range(0, 500000)):
        try:
            with open('./temp.txt', encoding='utf-8', mode='a') as file:
                file.write(str(i) + '\n')
            file.close()
        except Exception as e:
            print('文件生成失败，原因为：', e)
    print('结束写入')