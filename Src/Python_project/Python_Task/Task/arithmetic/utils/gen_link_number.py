# auth: code_king
# time: 2022/10/27 15:07
# file: gen_link_number.py
import copy
from typing import Any

smiles_list = ['56', '53', '(', '57', ')', '55', '(', '63', ')', '(', '62', ')', '61', '(', '67', ')', '(', '66', ')',
               '58', '(', '65', ')', '(', '64', ')', '54', '(', '60', ')', '(', '59', ')', '52', '68', '(', '71', ')',
               '70', '(', '77', ')', '(', '76', ')', '75', '(', '81', ')', '(', '80', ')', '78', '(', '83', '111',
               '112', '(', '115', ')', '(', '114', ')', '113', '(', '118', ')', '(', '117', ')', '116', ')', '(', '82',
               ')', '72', '(', '69', '(', '74', ')', '73', ')', '(', '79', ')', '93', '(', '99', ')', '98', '(', '106',
               ')', '103', '(', '110', ')', '(', '109', ')', '97', '(', '105', ')', '(', '104', ')', '92', '(', '95',
               '(', '101', ')', '(', '100', ')', '102', '(', '108', ')', '107', ')', '(', '96', ')', '91', '(', '94',
               ')', '88', '(', '90', ')', '(', '89', ')', '2', '3', '(', '8', ')', '4', '10', '(', '12', '17', '(',
               '16', '(', '20', ')', '15', '(', '19', ')', '14', '(', '84', '(', '87', ')', '(', '86', ')', '85', ')',
               '13', '18', ')', '5', '6', '(', '9', ')', '1', '7', ')', '(', '11', ')', '21', '23', '(', '27', ')',
               '26', '32', '(', '37', ')', '36', '(', '42', ')', '41', '46', '(', '49', ')', '48', '(', '51', ')', '44',
               '47', '(', '50', ')', '45', '(', '128', ')', '40', '43', '127', '(', '130', ')', '(', '129', ')', '124',
               '(', '126', ')', '(', '125', ')', '121', '(', '123', ')', '(', '122', ')', '119', '(', '120', ')', '38',
               '33', '28', '(', '24', '22', '25', '(', '31', ')', '30', ')', '34', '39', '35', '29']
bradk_graph = {'1': ['2'], '2': ['1'], '3': [], '4': ['5'], '5': ['4'], '6': [], '7': [], '8': [], '9': [], '10': [],
               '11': [], '12': ['13'], '13': ['12'], '14': [], '15': [], '16': [], '17': [], '18': [], '19': [],
               '20': [], '21': ['22'], '22': ['21'], '23': [], '24': ['29'], '25': [], '26': ['29'], '27': [], '28': [],
               '29': ['26', '24'], '30': ['52', '33'], '31': [], '32': [], '33': ['30'], '34': ['40'], '35': ['41'],
               '36': [], '37': [], '38': ['43'], '39': ['44'], '40': ['34'], '41': ['35'], '42': [], '43': ['38'],
               '44': ['39'], '45': [], '46': [], '47': [], '48': [], '49': [], '50': [], '51': [], '52': ['30', '53'],
               '53': ['52'], '54': [], '55': [], '56': [], '57': [], '58': [], '59': [], '60': [], '61': [], '62': [],
               '63': [], '64': [], '65': [], '66': [], '67': [], '68': ['69'], '69': ['68'], '70': [], '71': [],
               '72': [], '73': [], '74': [], '75': [], '76': [], '77': [], '78': [], '79': [], '80': [], '81': [],
               '82': [], '83': [], '84': [], '85': [], '86': [], '87': [], '88': [], '89': [], '90': [], '91': ['93'],
               '92': [], '93': ['91'], '94': [], '95': [], '96': [], '97': [], '98': ['102'], '99': [], '100': [],
               '101': [], '102': ['98'], '103': [], '104': [], '105': [], '106': [], '107': [], '108': [], '109': [],
               '110': [], '111': [], '112': [], '113': [], '114': [], '115': [], '116': [], '117': [], '118': [],
               '119': [], '120': [], '121': [], '122': [], '123': [], '124': [], '125': [], '126': [], '127': [],
               '128': [], '129': [], '130': []}


def get_usable_numbers(c_atoms: int = None):
    """
    :param c_atoms: C原子个数
    :return: 总共的键数
    """
    all_numbers = c_atoms * 3
    temp_list = []
    for i in range(1, all_numbers + 1):
        if i < 10:
            temp_list.append(str(i))
        else:
            temp_list.append(f'{i}')
    return temp_list


def get_atom_link(bradk_graph=None, smiles_list=None):
    """
    :param bradk_graph: 断键关系的字典
    :param smiles_list: smiles的中的原子
    :return: smiles的中有断掉关系的原子
    """
    temp_list = []
    atom_link = []
    for i in smiles_list:
        if i != '(' and i != ')':
            temp_list.append(i)
    # 只保留有连接关系的原子
    copy_bradk_graph = copy.deepcopy(bradk_graph)
    full_bradk_graph = get_full_break_graph(copy_bradk_graph=copy_bradk_graph, smiles_index=smiles_index)
    for i in temp_list:
        if i in full_bradk_graph.keys():
            atom_link.append(i)
    return atom_link


def get_mark_dict(atom_link: list = None, usable_numbers=None):
    """
    :param atom_link: smile中有连接关系的字典
    :param usable_numbers: 可以用的数字
    :return: 加好数字的字典
    """
    full_break_graph, break_link_graph = gen_break_link(bradk_graph=bradk_graph, smiles_index=smiles_index)
    original_atom_link = copy.deepcopy(usable_numbers)
    for i in atom_link:
        for item in range(0, len(full_break_graph[str(i)])):
            item = full_break_graph[str(i)][item]
            # 加连接关系
            add_number = usable_numbers.pop(0)
            break_link_graph[str(i)].append(add_number)
            break_link_graph[str(item)].append(f'&{add_number}')
            # 删除连接关系
            full_break_graph[str(i)].remove(str(item))
            full_break_graph[str(item)].remove(str(i))
        for k in range(len(break_link_graph[str(i)])):
            if '&' in break_link_graph[str(i)][k]:
                # 元素回位置，最后排序
                temp = break_link_graph[str(i)][k].replace('&', '')
                usable_numbers.append(temp)
        usable_numbers.sort(key=original_atom_link.index)
    # 将 '&'去掉，然后超过10的全部加上%
    for i in break_link_graph:
        for item in range(len(break_link_graph[str(i)])):
            if '&' in break_link_graph[str(i)][item]:
                break_link_graph[str(i)][item]=break_link_graph[str(i)][item].replace('&', '')
            if int(break_link_graph[str(i)][item]) > 10:
                break_link_graph[str(i)][item] = f'%{break_link_graph[str(i)][item]}'
    return break_link_graph


def get_ascend_break_graph(smiles_list=None):
    """
    :param smiles_list: 生成smiles的列表 如 ['1', '(','2',')' '3']
    :return: 只剩下smiles的原子的列表 如 ['1', '2', '3']
    """
    atom_smiles_list = []
    # 只留下原子的smiles
    for item in smiles_list:
        if item != '(' and item != ')':
            atom_smiles_list.append(item)
    smiles_index = {}
    for i in range(1, len(atom_smiles_list) + 1):
        smiles_index[str(i)] = ''
    # 获取smiles里面所有元素的索引
    for item in atom_smiles_list:
        smiles_index[str(item)] = atom_smiles_list.index(item)
    return atom_smiles_list, smiles_index


def sort_list(aim_list=None, index_list=None):
    """
    :param aim_list: 需要排序的列表
    :param index_list: 列表元素在smiles中的顺序，越小的索引要排在前面
    :return: 排好序列的列表
    """
    temp_list: list[Any] = []
    deal_aim_list = copy.deepcopy(aim_list)
    # 排序
    index = 1
    deal_aim_list_length = len(deal_aim_list)
    while index < deal_aim_list_length + 1:
        min_index = int(index_list[deal_aim_list[0]])
        temp_item = deal_aim_list[0]
        for i in deal_aim_list:
            if index_list[i] < int(min_index):
                min_index = int(index_list[i])
                temp_item = i
        temp_list.append(temp_item)
        deal_aim_list.remove(str(temp_item))
        index += 1
    return temp_list


def get_full_break_graph(copy_bradk_graph=None, smiles_index=None):
    """
    :param copy_bradk_graph: 还未排序的 非空字典列表
    :return: 排序的 非空字典列表
    """
    temp_full_break_graph = copy.deepcopy(copy_bradk_graph)
    index = 1
    original_length = len(temp_full_break_graph)
    while index < original_length + 1:
        if len(temp_full_break_graph[str(index)]) == 0:
            del temp_full_break_graph[str(index)]
        index += 1
    # 将连接顺序排好
    for item in temp_full_break_graph:
        if len(temp_full_break_graph[str(item)]) > 1:
            # 排序
            temp_full_break_graph[str(item)] = sort_list(aim_list=temp_full_break_graph[str(item)],
                                                         index_list=smiles_index)
    return temp_full_break_graph


# def add_numbers(recursion_list=None, max_number=None):
#     for item in recursion_list:
#         if item in full_bradk_graph:
#             max_number += 1
#         # 不在集合内
#         inner_start_index = atom_smiles_list.index(item)
#         inner_end = full_bradk_graph[str(item)][0]
#         inner_end_index = atom_smiles_list.index(inner_end)
#         temp_list = atom_smiles_list[inner_start_index:inner_end_index + 1]
#         return add_numbers(recursion_list=temp_list, max_number=max_number)
# def gen_connection_number(recursion_list=None, max_number=None):
#     for item in atom_smiles_list:
#         # 判断有断键关系
#         if item in full_bradk_graph:
#             if item in recursion_list:
#                 max_number += 1
#                 # 找到下一个集合
#                 inner_start_index = atom_smiles_list.index(item)
#                 inner_end = full_bradk_graph[str(item)][0]
#                 inner_end_index = atom_smiles_list.index(inner_end)
#                 temp_list = atom_smiles_list[inner_start_index:inner_end_index + 1]
#                 return gen_connection_number(recursion_list=temp_list, max_number=max_number)
#             else:
#                 inner_start_index = atom_smiles_list.index(item)
#                 inner_end = full_bradk_graph[str(item)][0]
#                 inner_end_index = atom_smiles_list.index(inner_end)
#                 temp_list = atom_smiles_list[inner_start_index:inner_end_index + 1]
#                 for i in temp_list:
#                     pass
#                 # 出口是 inner_end
#                 if atom_smiles_list.index(item) > atom_smiles_list.index(inner_end):
#                     pass
# max_number = 0
# # 把当前原子所有的断键关系加上数字
# index = 0
# full_bradk_graph_item_length = len(full_bradk_graph[str(item)])
# while index < full_bradk_graph_item_length:
#     atom_item = full_bradk_graph[str(item)][index]
#     # 开始加数字,需要判断里面已经有没有数字，两边的都要判断，并且取最大的
#     if break_link_graph[str(item)]:
#         if int(break_link_graph[str(item)][-1]) > max_number:
#             max_number = int(break_link_graph[str(item)][-1])
#     if break_link_graph[str(atom_item)]:
#         if int(break_link_graph[str(atom_item)][-1]) > max_number:
#             max_number = int(break_link_graph[str(atom_item)][-1])
#     insert_number = max_number + 1
#     # 需要判断数字是否大于10，大于10加 %
#     if insert_number >= 10:
#         insert_number = f'%{insert_number}'
#     break_link_graph[str(item)].append(str(insert_number))
#     break_link_graph[str(atom_item)].append(str(insert_number))
#     # 需要删除他俩的连接关系
#     full_bradk_graph[str(item)].remove(atom_item)
#     full_bradk_graph[str(atom_item)].remove(item)
#     index += 1

def gen_break_link(bradk_graph=None, smiles_index=None):
    """
    :param bradk_graph: 断键关系的图
    # :param atom_smiles_list: smiles的原子的列表 如 ['1', '2', '3']
    :param smiles_index:  smiles的原子的列表的索引，是一个字典类型{}
    :return:full_bradk_graph存放断键关系（排好序）,break_link_graph 是一个字典，存断的数字关系
    """
    # 只保留有链接关系的键值对
    copy_bradk_graph = copy.deepcopy(bradk_graph)
    full_break_graph = get_full_break_graph(copy_bradk_graph=copy_bradk_graph, smiles_index=smiles_index)
    # 记录断键原子的连接关系
    break_link_graph = {}
    for i in full_break_graph:
        break_link_graph[str(i)] = []
    return full_break_graph, break_link_graph


if __name__ == '__main__':
    atom_smiles_list, smiles_index = get_ascend_break_graph(smiles_list=smiles_list)
    full_bradk_graph, break_link_graph = gen_break_link(bradk_graph=bradk_graph, smiles_index=smiles_index)
    print(f'full_bradk_graph:{full_bradk_graph}')
    print(f'break_link_graph:{break_link_graph}')
    atom_link = get_atom_link(bradk_graph=bradk_graph, smiles_list=smiles_list)
    usable_numbers = get_usable_numbers(c_atoms=10)
    print(f'atom_link:{atom_link}')
    print(f'usable_numbers:{usable_numbers}')
    mark_dict = get_mark_dict(atom_link=atom_link, usable_numbers=usable_numbers)
    print(f'mark_dict:{mark_dict}')
