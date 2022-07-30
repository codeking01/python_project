"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/6/18 23:55
    @File : PreDeal_Tools.py
"""
from copy import copy
from math import ceil

# 所有的方法汇总
# 先判断缺失数据的的条件 这个以百分之70为基准
import numpy as np

def Del_deletion_data(datavalue, flag):
    # 删除缺失值过多的列
    if flag == 1:
        del_cols = []
        # 先拿到元数据的长度
        baseLength = datavalue.shape[0]
        # 这个 用来保存需要删除的列
        iterLength = datavalue.shape[1]
        for i in range(iterLength):
            temp = []
            temp = np.where(np.isnan(datavalue[:, i].astype(float)) == True)[0].tolist() + temp
            # print(temp)
            # 用集合去重
            c = set(temp)
            # 计算缺失的总行数
            lack_of_rows = len(c)
            if lack_of_rows > 0.3 * baseLength:
                del_cols.append(i)
                # print(datavalue)
        # flag是1则删除列，如果是0则删除行
        final_data = np.delete(datavalue, del_cols, axis=flag)
        # elif flag == 0:
        #     del_raws=[]+temp
        return final_data, del_cols
    # 删除含有缺失值的行
    elif flag == 0:
        # 筛选出含有缺失值的行，用set去重
        del_raws = set(np.where(np.isnan(datavalue.astype(float)) == True)[0].tolist())
        del_raws = list(del_raws)
        final_data = np.delete(datavalue, del_raws, axis=flag)
    return final_data


# 将 数据比较一下:① 必须是两边都有的数据才可以进行预测或者建模，②数据量必须是超过70%
def Record_usable_cols(datavalue):
    # 先拿到元数据的长度
    baseLength = datavalue.shape[0]
    iterLength = datavalue.shape[1]
    # 这个 用来保存需要删除的列
    del_cols = []
    for i in range(iterLength):
        temp = []
        # 根据缺失值，将索引存到列表中
        temp = np.where(np.isnan(datavalue[:, i].astype(float)) == True)[0].tolist() + temp
        # print(temp)
        # 用集合去重
        c = set(temp)
        # 计算缺失的总行数
        lack_of_rows = len(c)
        if (lack_of_rows < 0.3 * baseLength):
            del_cols.append(i)
            # print(datavalue)
    return del_cols


# 将两个数据的能用的列合并 判断两边的数据是否都存在
# Original_Ydata_usableCols = Record_usable_cols(Original_Ydata)
# pred_Ydata_usableCols = Record_usable_cols(pred_Ydata)
# final_cols = list(set(Original_Ydata_usableCols + pred_Ydata_usableCols))
# 这个里面的内容可以用来建模与预测
# final_cols

# 更改Y_data的为-1 0 1 获取Y_data,然后获取5%的边界最小值Y_data_boundsMin，和95%的边界最大值Y_data_boundsMax
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
# 替换为-1，0，1的分类
# temp_data = Deal_sorted_Ydata(Y_data)
# Y_data = temp_data[0]
# Y_data_boundsMin = temp_data[1]
# Y_data_boundsMax = temp_data[2]


# 处理带关键字的
def convert_to_num(dealdata):
    # 取出每一列的唯一值
    unique_value = np.unique(dealdata)
    index = -1
    # 把关键字挨个处理
    for i in unique_value:
        dealdata = np.where(dealdata == f"{i}", index, dealdata)
        index += 1
    return dealdata


# 删除多余的列，并且返回处理好的数据已经需要删除的列
def delAndGetCols(deal_value):
    # 删除部分的缺失值过多的列
    temp_TwoToThree_Xdata = Del_deletion_data(deal_value, 1)
    base_temp_TwoToThree_Xdata = temp_TwoToThree_Xdata[0]
    # 获取需要删除的列
    del_cols = temp_TwoToThree_Xdata[1]
    return base_temp_TwoToThree_Xdata, del_cols


# 获取可用的列
def get_final_useablecols(Original_Yvalue, Pred_Yvalue):
    # 将两个数据的能用的列合并 判断两边的数据是否都存在
    Original_Ydata_usableCols = Record_usable_cols(Original_Yvalue)
    pred_Ydata_usableCols = Record_usable_cols(Pred_Yvalue)
    # 取出交集
    # list(set(a).intersection(b))
    final_cols = list(set(Original_Ydata_usableCols).intersection(pred_Ydata_usableCols))
    # final_cols = list(set(Original_Ydata_usableCols + pred_Ydata_usableCols))
    # 这个里面的内容可以用来建模与预测(可用的列)
    return final_cols


# 获取所有的Ydata(从final_cols中获取)
def all_ydata(final_cols, original_yvalue, pred_yvalue):
    # 取出Y_data 元数据
    # 用来存储所有的Y_data
    Original_YdataList = []
    Pred_YdataList = []
    for index in final_cols:
        Original_YdataList.append(original_yvalue[:, index])
        Pred_YdataList.append(pred_yvalue[:, index])
    return Original_YdataList, Pred_YdataList

# 根据传入的excel对象，将数据表合并
def get_merge_tabledata(excel_data):
    # 这个数据是公共部分 需要转化为数字
    Commonhead = excel_data[3:, 4:6]
    # 替换的方法 取出第1列
    Commonhead[:, 0] = convert_to_num(Commonhead[:, 0])
    Commonhead[:, 1] = convert_to_num(Commonhead[:, 1])
    # 处理表1和表2
    TABLE_ONE = excel_data[3:, 6:19]
    # 这个地方必须转成字符串   处理掉汉字
    TABLE_ONE[:, 12] = convert_to_num(TABLE_ONE[:, 12].astype(str))
    TABLE_TWO = excel_data[3:, 19:23]
    # 处理表3
    TABLE_THREE = excel_data[3:, 61:66]
    # 这个地方必须转成字符串   处理掉汉字
    TABLE_THREE[:, -1] = convert_to_num(TABLE_THREE[:, -1].astype(str))
    # 处理表4
    TABLE_FOUR = excel_data[3:, 88:101]
    TABLE_FOUR[:, -1] = convert_to_num(TABLE_FOUR[:, -1].astype(str))
    # 处理表5
    TABLE_FIVE = excel_data[3:, 101:107]
    TABLE_FIVE[:, -1] = convert_to_num(TABLE_FIVE[:, -1].astype(str))
    # 处理表6
    TABLE_SIX = excel_data[3:, 131:144]
    TABLE_SIX[:, -1] = convert_to_num(TABLE_SIX[:, -1].astype(str))
    # 处理表7
    TABLE_SEVEN = excel_data[3:, 172:178]
    TABLE_SEVEN[:, -1] = convert_to_num(TABLE_SEVEN[:, -1].astype(str))
    # 合并一下数据
    mergeTwo_data = np.column_stack((Commonhead, TABLE_ONE, TABLE_TWO))
    mergeThree_data = np.column_stack((mergeTwo_data, TABLE_THREE))
    mergeFour_data = np.column_stack(( mergeThree_data, TABLE_FOUR))
    mergeFive_data = np.column_stack((mergeFour_data, TABLE_FIVE))
    mergeSix_data = np.column_stack((mergeFive_data, TABLE_SIX))
    mergeSeven_data = np.column_stack((mergeSix_data, TABLE_SEVEN))
    return mergeTwo_data, mergeThree_data, mergeFour_data, mergeFive_data, mergeSix_data, mergeSeven_data

# 根据传入的excel对象获取Y数据
def get_former_Ydata(excel_data):
    # 处理所有建模的Y_data
    Merge_TableTwoYdata = excel_data[3:, 23:61]
    Merge_TableThreeYdata = excel_data[3:, 66:88]
    # 没有Original_TableFourYdata
    Merge_TableFiveYdata = excel_data[3:, 107:131]
    Merge_TableSixYdata = excel_data[3:, 144:172]
    Merge_TableSevenYdata = excel_data[3:, 178:249]
    return Merge_TableTwoYdata, Merge_TableThreeYdata, Merge_TableFiveYdata, Merge_TableSixYdata, Merge_TableSevenYdata

# 根据Y_data_boundsMin和Y_data_boundsMax处理Y_data
def deal_verify_ydata(Verify_Ydata,Y_data_boundsMin,Y_data_boundsMax):
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
    return Verify_Ydata
