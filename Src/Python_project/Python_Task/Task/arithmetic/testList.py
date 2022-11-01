# auth: code_king
# time: 2022/10/21 14:23
# file: testList.py

test = [['7'], ['9'], ['20'], ['19'], ['86'], ['85'], ['18'], ['129'], ['125'], ['122'], ['76'], ['80'], ['114'],
        ['117'], ['116'], ['82'], ['109'], ['104'], ['100'], ['107'], ['89'], ['79'], ['73'], ['59'], ['64'], ['66'],
        ['62'], ['56'], ['22'], ['11'], ['84', '87'], ['36', '42'], ['48', '51'], ['45', '128'], ['124', '126'],
        ['121', '123'], ['119', '120'], ['70', '77'], ['75', '81'], ['113', '118'], ['98', '106'], ['103', '110'],
        ['97', '105'], ['92', '96'], ['95', '101'], ['102', '108'], ['91', '94'], ['88', '90'], ['69', '74'],
        ['54', '60'], ['58', '65'], ['61', '67'], ['55', '63'], ['53', '57'], ['25', '31'], ['28', '24'],
        ['21', '23', '27'], ['26', '32', '37'], ['41', '46', '49'], ['44', '47', '50'], ['72', '93', '99'],
        ['40', '43', '127', '130'], ['34', '39', '35', '29'], ['78', '83', '111', '112', '115'],
        ['38', '33', '30', '52', '68', '71']]
# item_index = 0
# while item_index < len(test):
# temp_list = []
# temp_list.append(test[item_index])
# if item_index != len(test) - 1:
#     for i in range(item_index + 1, len(test)):
#         if len(test[item_index]) < len(test[i]):
#             item_index = i
#             break
#         else:
#             item_index += 1
#             temp_list.append(test[i])
#     print('***', temp_list)
# else:
#     print('***', temp_list)
#     break

# 倒序遍历
# for i in range(len(test) - 1, -1, -1):
#     test[0] = '***************************'
#     print('***', test[i])


# 将长度记录下来，相同长度的放在一个列表所以里
index_list = [len(i) for i in test]
print(index_list)


def get_traverse_list(index_list=None):
    '''
    :param index_list: 传入带有长度的列表
    :return: 返回遍历的列表
    '''
    flag_index = []
    start_flag = True
    for i in range(0, len(index_list)):
        if start_flag == True:
            start = i
            end = i
            start_flag = False
        if i != len(index_list) - 1:
            if index_list[i] == index_list[i + 1]:
                end += 1
            else:
                flag_index.append([start, end])
                start_flag = True
        else:
            # 单独处理最后一个元素
            if start_flag == False:
                flag_index.append([start, end])
    return flag_index


def deal_data(side_set_list=None, flag_index=None):
    for flag_item in flag_index:
        # 先处理单原子
        if len(side_set_list[flag_item[0]]) == 1:
            for single_atom_index in range(flag_item[0], flag_item[-1] + 1):
                print(side_set_list[single_atom_index])
        else:
            # 处理多个原子的情况 flag_item[1]是列表的后面一个元素，代表结束索引
            for single_atom_index in range(flag_item[1], flag_item[0] - 1, -1):
                # 找到单个集合的
                if flag_item[0] == flag_item[1]:
                    print('单个集合：', side_set_list[single_atom_index])
                # print(side_set_list[single_atom_index])


print('********************************')
flag_index = get_traverse_list(index_list=index_list)
print('flag_index：', flag_index)
deal_data(side_set_list=test, flag_index=flag_index)


def get_rest_side_atoms(start_point=None, aim_list=None):
    rest_list = []
    for i in range(start_point, len(aim_list)):
        # 面侧链所有原子,里面可能带侧链，['a','('d','('e')')','c']
        for k in aim_list[i]:
            if '(' not in k and ')' not in k:
                rest_list.append(k)
    return rest_list


print('********************************')
temp_list = get_rest_side_atoms(start_point=11, aim_list=test)
print('temp_list', temp_list)
