"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/6/19 0:01
    @File : BuildIngModel.py
"""
from numpy import unique
from src.OtherTasks.ML.PreDeal_Tools import Del_deletion_data, Record_usable_cols, Deal_sorted_Ydata, convert_to_num, \
    get_final_useablecols, all_ydata, delAndGetCols
from math import ceil
from copy import copy
import pandas as pd
import numpy as np

def Deal_sorted_Ydata(data):
    # 用来记录原顺序的数组，取反
    # order = np.argsort(-data)
    sort_data = copy(data)
    sort_data = sorted(sort_data)
    # sorted返回的是数组类型，这个地方需要转成ndarray
    sort_data = np.array(sort_data)
    data_length = sort_data.shape[0]
    # 根据5%为1，中间90%为0，后5%为-1
    # 这个地方要考虑临界条件，当处于临界条件的值，全部分配给两端
    bound_min_value = sort_data[int(ceil(0.05 * data_length))]
    bound_max_value = sort_data[int(ceil(0.95 * data_length))]
    # print('min长度', int(ceil(0.05 * data_length)))
    # print(bound_min_value, bound_max_value)
    min_data = np.where(data <= bound_min_value)
    # print('min_data', min_data)
    max_data = np.where(data >= bound_max_value)
    # print('max_data', max_data)
    normal_data = np.where((data > bound_min_value) & (data < bound_max_value))
    # print('normal_data', normal_data)
    # 统一进行替换为-1，1，0
    data[min_data] = -1
    data[max_data] = 1
    data[normal_data] = 0
    # data[0:int(data_length*0.05)]=1
    # data[int(data_length*0.05):int(data_length*0.95)]=0
    # data[int(data_length*0.95):]=-1
    # 恢复原来的顺序
    # recovery_arr = np.zeros_like(data)
    # for idx, num in enumerate(data):
    #     recovery_arr[order[idx]] = num
    return data, bound_min_value, bound_max_value


if __name__ == '__main__':


    # 这个pandas处理数据效果不太好 建议用numpy
    thedata = pd.read_excel(io='Data613.xlsx', sheet_name='数据标准化-建模用')
    Preddata = pd.read_excel(io='Data613.xlsx', sheet_name='数据标准化-预测用')

    thedata = np.array(thedata)
    Preddata = np.array(Preddata)
    # 将表的内容 7个数据表 挨个处理

    # 这个数据是公共部分 需要转化为数字
    Commonhead = thedata[3:, 4:6]
    # 替换的方法 取出第1列
    Commonhead[:, 0] = convert_to_num(Commonhead[:, 0])
    Commonhead[:, 1] = convert_to_num(Commonhead[:, 1])
    # 处理所有的X_data
    # 处理表1和表2
    TABLE_ONE = thedata[3:, 6:19]
    # 这个地方必须转成字符串   处理掉汉字
    TABLE_ONE[:, 12] = convert_to_num(TABLE_ONE[:, 12].astype(str))
    TABLE_TWO = thedata[3:, 19:23]
    # 处理表3
    TABLE_THREE = thedata[3:, 61:66]
    # 这个地方必须转成字符串   处理掉汉字
    TABLE_THREE[:, -1] = convert_to_num(TABLE_THREE[:, -1].astype(str))
    # 处理表4
    TABLE_FOUR = thedata[3:, 88:101]
    TABLE_FOUR[:, -1] = convert_to_num(TABLE_FOUR[:, -1].astype(str))
    # 处理表5
    TABLE_FIVE = thedata[3:, 101:107]
    TABLE_FIVE[:, -1] = convert_to_num(TABLE_FIVE[:, -1].astype(str))
    # 处理表6
    TABLE_SIX = thedata[3:, 131:144]
    TABLE_SIX[:, -1] = convert_to_num(TABLE_SIX[:, -1].astype(str))
    # 处理表7
    TABLE_SEVEN = thedata[3:, 172:178]
    TABLE_SEVEN[:, -1] = convert_to_num(TABLE_SEVEN[:, -1].astype(str))
    # 合并一下数据
    FormerTwo_data = np.column_stack((Commonhead, TABLE_ONE, TABLE_TWO))
    FormerThree_data = np.column_stack((FormerTwo_data, TABLE_THREE))
    FormerFour_data = np.column_stack((FormerThree_data, TABLE_FOUR))
    FormerFive_data = np.column_stack((FormerFour_data, TABLE_FIVE))
    FormerSix_data = np.column_stack((FormerFive_data, TABLE_SIX))
    FormerSeven_data = np.column_stack((FormerSix_data, TABLE_SEVEN))
    tempFormerTwo_data = delAndGetCols(FormerTwo_data)
    base_Xdata = tempFormerTwo_data[0]
    del_cols = tempFormerTwo_data[1]
    # 处理所有建模的Y_data
    Original_TableTwoYdata = thedata[3:, 23:61]
    Original_TableThreeYdata = thedata[3:, 66:88]
    # 没有Original_TableFourYdata
    Original_TableFiveYdata = thedata[3:, 107:131]
    Original_TableSixYdata = thedata[3:, 144:172]
    Original_TableSevenYdata = thedata[1:, 178:249]
    # 处理所有预测的Y_data
    Pred_TableTwoYdata = Preddata[3:, 23:61]
    Pred_TableThreeYdata = Preddata[3:, 66:88]
    # 没有Pred_TableFourYdata
    Pred_TableFiveYdata = Preddata[3:, 107:131]
    Pred_TableSixYdata = Preddata[3:, 144:172]
    Pred_TableSevenYdata = Preddata[1:, 178:249]
    # 将Y取出来，然后取出缺失值过多的列 # 获取可用的列
    final_cols = get_final_useablecols(Original_TableTwoYdata, Pred_TableTwoYdata)
    # 获取可以用的Y_data
    Original_YdataList, Pred_YdataList = all_ydata(final_cols, Original_TableTwoYdata, Pred_TableTwoYdata)
    # todo 到时候遍历这个列表，然后依次计算
    # 建模的Y_data
    Modeling_Y_data = Original_YdataList[8]
    # 预测的Y_data
    Pred_Y_data = Pred_YdataList[8]
    temp_OriginalXdata = np.column_stack((base_Xdata, Modeling_Y_data))
    # 删除缺失的行
    temp_OriginalXdata = Del_deletion_data(temp_OriginalXdata, 0)
    X_data = temp_OriginalXdata[:, :-1]
    Y_data = temp_OriginalXdata[:, -1]

    # 检验一下是否将所有的空值删除完毕，这个地方是用来做验证的 返回为空列表则删除成功！
    print('为[],则说明全部缺失值的行删除完毕!', list(set(np.where(np.isnan(temp_OriginalXdata.astype(float)) == True)[0].tolist())))
    Y_data, Y_data_boundsMin, Y_data_boundsMax = Deal_sorted_Ydata(Y_data)
    # 查看是否替换成功
    print(unique(Y_data), Y_data_boundsMin, Y_data_boundsMax)
    # 获取预测数据
    Verify_Ydata = Pred_Y_data
    # 将pred_Ydata 替换成-1，0，1的分类
    min_data = np.where(Verify_Ydata <= Y_data_boundsMin)
    # print('min_data', min_data)
    max_data = np.where(Verify_Ydata >= Y_data_boundsMax)
    # print('max_data', max_data)
    normal_data = np.where((Verify_Ydata > Y_data_boundsMin) & (Verify_Ydata < Y_data_boundsMax))
    # print('normal_data', normal_data)
    # 统一进行替换为-1，1，0
    Verify_Ydata[min_data] = -1
    Verify_Ydata[max_data] = 1
    Verify_Ydata[normal_data] = 0
    print(np.unique(Verify_Ydata))
