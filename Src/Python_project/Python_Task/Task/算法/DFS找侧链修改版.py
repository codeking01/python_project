import time
from typing import List

graph = {1: [2, 6, 7],
         2: [1, 3, 88],
         3: [2, 4, 8],
         4: [3, 5, 10],
         5: [4, 6, 17],
         6: [1, 5, 9],
         7: [1],
         8: [3],
         9: [6],
         10: [4, 11, 12, 21],
         11: [10],
         12: [10, 13, 17],
         13: [12, 14, 18],
         14: [13, 15, 84],
         15: [14, 16, 19],
         16: [15, 17, 20],
         17: [5, 12, 16],
         18: [13],
         19: [15],
         20: [16],
         21: [10, 22, 23],
         22: [21, 24, 25],
         23: [21, 26, 27],
         24: [22, 28, 29],
         25: [22, 30, 31],
         26: [23, 29, 32],
         27: [23],
         28: [24, 33, 34],
         29: [24, 26, 35],
         30: [25, 33, 52],
         31: [25],
         32: [26, 36, 37],
         33: [28, 30, 38],
         34: [28, 39, 40],
         35: [29, 39, 41],
         36: [32, 41, 42],
         37: [32],
         38: [33, 43, 119],
         39: [34, 35, 44],
         40: [34, 43, 45],
         41: [35, 36, 46],
         42: [36],
         43: [38, 40, 127],
         44: [39, 47, 48],
         45: [40, 47, 128],
         46: [41, 48, 49],
         47: [44, 45, 50],
         48: [44, 46, 51],
         49: [46],
         50: [47],
         51: [48],
         52: [30, 53, 54, 68],
         53: [52, 55, 56, 57],
         54: [52, 58, 59, 60],
         55: [53, 61, 62, 63],
         56: [53],
         57: [53],
         58: [54, 61, 64, 65],
         59: [54],
         60: [54],
         61: [55, 58, 66, 67],
         62: [55],
         63: [55],
         64: [58],
         65: [58],
         66: [61],
         67: [61],
         68: [52, 69, 70, 71],
         69: [68, 72, 73, 74],
         70: [68, 75, 76, 77],
         71: [68],
         72: [69, 78, 79, 93],
         73: [69],
         74: [69],
         75: [70, 78, 80, 81],
         76: [70],
         77: [70],
         78: [72, 75, 82, 83],
         79: [72],
         80: [75],
         81: [75],
         82: [78],
         83: [78, 111],
         84: [14, 85, 86, 87],
         85: [84],
         86: [84],
         87: [84],
         88: [2, 89, 90, 91],
         89: [88],
         90: [88],
         91: [88, 92, 93, 94],
         92: [91, 95, 96, 97],
         93: [72, 91, 98, 99],
         94: [91],
         95: [92, 100, 101, 102],
         96: [92],
         97: [92, 103, 104, 105],
         98: [93, 102, 103, 106],
         99: [93],
         100: [95],
         101: [95],
         102: [95, 98, 107, 108],
         103: [97, 98, 109, 110],
         104: [97],
         105: [97],
         106: [98],
         107: [102],
         108: [102],
         109: [103],
         110: [103],
         111: [83, 112],
         112: [111, 113, 114, 115],
         113: [112, 116, 117, 118],
         114: [112],
         115: [112],
         116: [113],
         117: [113],
         118: [113],
         119: [38, 120, 121],
         120: [119],
         121: [119, 122, 123, 124],
         122: [121],
         123: [121],
         124: [121, 125, 126, 127],
         125: [124],
         126: [124],
         127: [43, 124, 129, 130],
         128: [45],
         129: [127],
         130: [127]}


# todo 引用传递的解决

# 将字典的键值全部改成字符串
def exchange_graph(graph=None):
    # 转成字符串
    for i in graph:
        graph[i] = [str(k) for k in graph[i]]

    for i in list(graph.keys()):
        graph[str(i)] = graph[i]
        del graph[i]
    return graph


def find_aim_atom(graph_item_list=None, aim_list=None):
    """
    :param graph_item_list:
    :param aim_list: 原子列表(主 侧都行)
    :return: 找到就返回原子，否则返回 ''
    """
    for graph_item in graph_item_list:
        if graph_item not in aim_list:
            continue
        else:
            # 记录目标原子
            return graph_item
    return ''


def record_atom_link(aim_atom=None, graph_item_list=None, erased_dic_list=None):
    """
    :param aim_atom: 目标原子，这个原子需要保持连接
    :param graph_item_list: 遍历的连接关系
    :param erased_dic_list: 记录断开的原子
    :return:
    """
    if erased_dic_list is None:
        erased_dic_list = []
    for graph_item in graph_item_list:
        if graph_item != aim_atom:
            erased_dic_list.append(graph_item)
    return erased_dic_list


def insert_aim_list(aim_list=None, aim_atom=None, insert_atom=None):
    """
    :param aim_list: 连接原子的节点
    :param aim_atom: 插入的原子
    :return:
    """
    # 将当前原子并到主链上去
    insert_index = aim_list.index(aim_atom)
    aim_list.insert(insert_index + 1, f'''({insert_atom})''')
    return aim_list


def find_insert_side_index(side_set_list=None, aim_atom=None, insert_atom=None):
    """
    :param side_set_list: 侧链的集合
    :param aim_atom: 要找的连接到的原子
    :param insert_atom: 要插入的原子
    :return: 返回插入好的侧链集合
    """
    for out_index in range(0, len(side_set_list)):
        if aim_atom in side_set_list[out_index]:
            # side_set_list.insert(side_set_list[out_index].index(aim_atom), f'({insert_atom})')
            side_set_list[out_index].insert(side_set_list[out_index].index(aim_atom) + 1, f'''({insert_atom})''')
            return side_set_list


def del_connection(erased_dic_item_list=None, graph=None, del_atom=None):
    """
    :param erased_dic_item_list: 要删除的序列，传入的是删除关系，如{'A':['B','C']},['B','C']是需要删除的序列。
    :param graph: 图
    :param del_atom: 与图绑定的连接起始点
    :return: 处理后的图
    """
    if len(erased_dic_item_list) != 0:
        for i in erased_dic_item_list:
            graph[i].remove(str(del_atom))
        return graph
    return graph


def get_traverse_list(index_list=None):
    """
    :param index_list: 传入带有长度的列表
    :return: 返回带头尾遍历的列表 [[0,5],[6,6],[7,8],[9,9]]
    """
    flag_index_list: list[list[int]] = []
    start_flag = True
    for i in range(0, len(index_list)):
        if start_flag:
            start = i
            end = i
            start_flag = False
        if i != len(index_list) - 1:
            if index_list[i] == index_list[i + 1]:
                end += 1
            else:
                flag_index_list.append([start, end])
                start_flag = True
        else:
            # 单独处理最后一个元素
            if not start_flag:
                flag_index_list.append([start, end])
    return flag_index_list


# 记录连接关系
def del_other_connections(graph=None, exclude_atoms=None, del_aim_atom=None, erased_dic_list=None):
    """
    :param graph: 记录连接关系的图 graph[del_aim_atom] 代表 del_aim_atom的连接关系如：['c', 'd']
    :param exclude_atoms: 排除的原子['a', 'c']，如果当前是头部原子，那么a原子是根原子，c是后面一个原子。这两个不能删除
    :param del_aim_atom: 当前需要删除的目标原子的连接关系如当前是 'b',连接关系如： a-b-c
    :param erased_dic_list: 用来记录删除后的连接关系，与del_aim_atom绑定,如果b除了a,c还连接d,e则删除并记录,如{'b': ['d', 'e'']'}
    :return: 返回记录删除关系的 列表[] erased_dic_list:[],会在erased_dic[x]去接受它
    """
    if erased_dic_list is None:
        erased_dic_list = []
    for item in graph[del_aim_atom]:
        if item not in exclude_atoms:
            graph[del_aim_atom].remove(item)
            # 记录相互删除关系
            erased_dic_list.append(item)
            # 其他原子与当前的原子也要删除
            del_connection(erased_dic_item_list=erased_dic_list, graph=graph, del_atom=del_aim_atom)
    return erased_dic_list


# 删除连接关系需要记录
def del_side_connections(graph=None, current_item_list=None, aim_atom=None, erased_dic=None):
    """
    :param erased_dic: 记录删除的连接关系 如{'b': ['d', 'e'']'}
    :param graph: 提供图的连接关系
    :param current_item_list: 当前的侧链单个列表 如[1,2,3,4]
    :param aim_atom: 连接的原子
    :return: graph 是删除好连接关系的  erased_dic记录删除关系
    """
    for side_item_index in range(len(current_item_list)):
        # 单独处理列表的头和尾部
        if side_item_index == 0:
            root_node = aim_atom
            next_node = current_item_list[side_item_index + 1]
            if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                continue
            else:
                del_aim_atom = current_item_list[side_item_index]
                erased_dic[str(del_aim_atom)] = del_other_connections(graph=graph, exclude_atoms=[root_node, next_node],
                                                                      del_aim_atom=del_aim_atom)
        elif side_item_index == len(current_item_list) - 1:
            pre_node = current_item_list[side_item_index - 1]
            if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                continue
            else:
                del_aim_atom = current_item_list[side_item_index]
                erased_dic[str(del_aim_atom)] = del_other_connections(graph=graph, exclude_atoms=[pre_node],
                                                                      del_aim_atom=del_aim_atom)
        # 处理中间的原子
        else:
            pre_node = current_item_list[side_item_index - 1]
            next_node = current_item_list[side_item_index + 1]
            if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                continue
            else:
                del_aim_atom = current_item_list[side_item_index]
                erased_dic[str(del_aim_atom)] = del_other_connections(graph=graph, exclude_atoms=[pre_node, next_node],
                                                                      del_aim_atom=del_aim_atom)
    return graph, erased_dic


# 找到主路原子连接关系
def find_main_atoms(current_item_list=None, graph=None, main_list=None, erased_dic=None):
    """
    :param current_item_list:
    :param graph:
    :param main_list:
    :param erased_dic:
    :return:
    """
    main_flag = False
    # 临时记录当前原子 current_item_list代表类似 [1，2，3，4]
    # 先从头尾去找主原子，先判断是不是在主链上，找到主原子
    if find_aim_atom(graph_item_list=graph[current_item_list[0]], aim_list=main_list) != '':
        main_flag = True
        aim_atom = find_aim_atom(graph_item_list=graph[current_item_list[0]], aim_list=main_list)
        # 提供graph,erased_dic
        graph, erased_dic = del_side_connections(graph=graph, current_item_list=current_item_list,
                                                 aim_atom=aim_atom, erased_dic=erased_dic)
        # 将当前原子并到主链上去
        main_list = insert_aim_list(aim_list=main_list, aim_atom=aim_atom,
                                    insert_atom=f'''{str(current_item_list).replace('[', '').replace(']', '')}''')

    elif find_aim_atom(graph_item_list=graph[current_item_list[-1]], aim_list=main_list) != '':
        main_flag = True
        aim_atom = find_aim_atom(graph_item_list=graph[current_item_list[-1]], aim_list=main_list)
        # 反转列表
        current_item_list.reverse()
        graph, erased_dic = del_side_connections(graph=graph, current_item_list=current_item_list,
                                                 aim_atom=aim_atom, erased_dic=erased_dic)
        main_list = insert_aim_list(aim_list=main_list, aim_atom=aim_atom,
                                    insert_atom=f'''{str(current_item_list).replace('[', '').replace(']', '')}''')
    return graph, erased_dic, main_list, main_flag


def get_rest_side_atoms(start_point=None, aim_list=None):
    """
    :param start_point: 起始索引
    :param aim_list: 目标列表，指的是侧链的列表剩下的元素
    :return: 侧链剩下的元素组成的列表
    """
    rest_list = []
    for i in range(start_point, len(aim_list)):
        for k in aim_list[i]:
            # 取出后面侧链所有原子,里面可能带侧链，['a','('d')','c']
            if '(' not in k and ')' not in k:
                rest_list.append(k)
    return rest_list


def deal_multiple_atoms(graph=None, main_list=None, side_set_list=None, flag_index: [] = None, erased_dic=None):
    """
    :type erased_dic: {}
    :param graph: 提供图的连接关系
    :param main_list: 当前的侧链单个列表graph:
    :param side_set_list:
    :param flag_index:
    :param erased_dic:
    :return:
    """
    for flag_item in flag_index:
        # 单原子之前处理过了，直接跳过即可
        if len(side_set_list[flag_item[0]]) == 1:
            continue
        else:
            # 处理多个原子的情况 flag_item[1]是列表的后面一个元素，代表结束索引（原序列）,但是我是倒着遍历的，所以是开始索引
            for single_atom_index in range(flag_item[1], flag_item[0] - 1, -1):
                # 单集合,和最后一个元素列表
                if side_set_list[flag_item[0]] == side_set_list[flag_item[1]]:
                    # 临时记录当前原子 current_item_list代表类似 [1，2，3，4]
                    current_item_list = side_set_list[flag_item[0]]
                    graph, erased_dic, main_list, main_flag = find_main_atoms(current_item_list=current_item_list,graph=graph,main_list=main_list,erased_dic=erased_dic)
                    if not main_flag:
                        # 判断原子是否在侧链上，一定在后面的集合找，不能去前面找，因为只能往后面并,如果后面没有集合了，那么一定在主路上
                        if flag_item != flag_index[-1]:
                            start_point = flag_index[flag_index.index(flag_item) + 1][0]
                            rest_side_atoms = get_rest_side_atoms(start_point=start_point, aim_list=side_set_list)
                            # 找上一级侧链连接原子
                            if find_aim_atom(graph_item_list=graph[current_item_list[0]], aim_list=rest_side_atoms)!='':
                                aim_atom = find_aim_atom(graph_item_list=graph[current_item_list[0]], aim_list=rest_side_atoms)
                                del_side_connections(graph=graph, current_item_list=current_item_list, aim_atom=aim_atom)
                                # 将当前原子并到侧链链上去
                                side_set_list = find_insert_side_index(side_set_list=side_set_list, aim_atom=aim_atom,insert_atom=f'''{str(current_item_list)}''')
                            elif  find_aim_atom(graph_item_list=graph[current_item_list[-1]], aim_list=rest_side_atoms)!='':
                                current_item_list.reverse()
                                aim_atom = find_aim_atom(graph_item_list=graph[current_item_list[0]], aim_list=rest_side_atoms)
                                del_side_connections(graph=graph, current_item_list=current_item_list, aim_atom=aim_atom)
                                side_set_list = find_insert_side_index(side_set_list=side_set_list, aim_atom=aim_atom,insert_atom=f'''{str(current_item_list)}''')
                        # 单集合且是最后一个元素，那么肯定是并到主链上
                        else:
                            graph, erased_dic, main_list, main_flag = find_main_atoms(current_item_list=current_item_list, graph=graph,main_list=main_list, erased_dic=erased_dic)
            print('\nside_set_list.....\n', side_set_list)
            # todo 将等长的侧链集合单独处理，

def find_side_path(graph=None, side_set_list=None, main_list=None, sideList=None, flag_index=None):
    erased_dic = {}
    item_index = 0
    while item_index < len(side_set_list):
        # for item_index in range(0,len(side_set_list)):
        if item_index != len(side_set_list) - 1:
            item = side_set_list[item_index]
            # 先判断只有一个原子的情况，将这个原子加到侧链上去，或者主链上，优先加到主链路（前提是与主链可以直接连接）
            # 加了以后，去掉该原子的其他连接，并且记录到字典中,并且删除graph中的连接关系,遍历存储的字典（erased_dic），删除当前节点的连接关系
            # 同时在遍历的时候，删除该遍历节点与这个当前节点的连接关系，graph[currentNode].remove(item)
            if len(item) == 1:
                # 先判断是不是在主链上，找到主原子
                if find_aim_atom(graph_item_list=graph[item[0]], aim_list=main_list) != '':
                    aim_atom = find_aim_atom(graph_item_list=graph[item[0]], aim_list=main_list)
                    # 记录删除的原子关系
                    erased_dic[str(item[0])] = record_atom_link(aim_atom=aim_atom, graph_item_list=graph[item[0]],
                                                                erased_dic_list=[])
                    # 删除除当前原子外的其他连接关系 ,其他和当前原子的连接关系也要断掉
                    graph[item[0]] = [aim_atom]
                    graph = del_connection(erased_dic_item_list=erased_dic[str(item[0])], graph=graph,
                                           del_atom=str(item[0]))
                    # 将当前原子并到主链上去
                    main_list = insert_aim_list(aim_list=main_list, aim_atom=aim_atom, insert_atom=item[0])
                else:
                    # 找上一级侧链连接原子
                    aim_atom = find_aim_atom(graph_item_list=graph[item[0]], aim_list=sideList)
                    # 这个一定能找到，记录删除的原子关系
                    erased_dic[str(item[0])] = record_atom_link(aim_atom=aim_atom, graph_item_list=graph[item[0]],
                                                                erased_dic_list=[])
                    # 然后就删掉除当前原子外的其他连接关系
                    graph[item[0]] = [aim_atom]
                    graph = del_connection(erased_dic_item_list=erased_dic[str(item[0])], graph=graph,
                                           del_atom=str(item[0]))
                    # 将当前原子并到侧边链上去,先将目标原子找到(找到所在的集合)，然后并上去
                    side_set_list = find_insert_side_index(side_set_list=side_set_list, aim_atom=aim_atom,
                                                           insert_atom=item[0])
                # 遍历序号加1
                item_index += 1
            # 处理侧链的集合
            # ① 只需要判断两侧端点的连接关系即可
            # ② 如果主链上没有找到连接关系，将它并到侧链上
            # ③ 删除该链路剩下的多余连接关系
            else:
                deal_multiple_atoms(graph=graph, main_list=main_list, side_set_list=side_set_list, flag_index= flag_index, erased_dic=erased_dic)
        else:
            # todo 最后一个元素，这个元素一定在主链上
            item_index += 1

    return side_set_list, erased_dic, main_list, graph


# 对侧链集合列表从小到大排序
def get_final_side(side_set_list=None):
    #  按照大小升序,先找到各个列表的大小
    if side_set_list is None:
        side_set_list = []
    set_num = set([len(item) for item in side_set_list])
    temp_list = []
    for i in set_num:
        for k in side_set_list:
            if len(k) == i:
                temp_list.append(k)
    return temp_list


# 找到侧链的集合列表
def find_side(graph, result):
    # 存储所有侧链的原子
    side_list = []
    # 存储所有侧链的集合列表
    side_set_list = []
    # 找到'#'的侧链
    for item in result:
        if '#' in item:
            item = item.replace("#", "")
            side_list.append(item)
    # print(side_list)
    # 临时集合列表
    temp_set_list = []
    # 找侧链的集合列表
    for index in range(0, len(side_list)):
        if index != len(side_list) - 1:
            # 没进去的话，先进一个
            if side_list[index] not in temp_set_list:
                temp_set_list.append(side_list[index])
            # 找相邻的两个原子是否有直接连接关系，有则放一起
            if side_list[index] in graph[side_list[index + 1]]:
                temp_set_list.append(side_list[index + 1])
            else:
                side_set_list.append(temp_set_list)
                temp_set_list = []
        else:
            # 最后一个原子需要再判断一下,如果前面一个没有和最后这个原子连续，则最后的原子单独成一个集合
            if side_list[index] not in side_set_list:
                side_set_list.append([side_list[index]])
            return side_set_list
            # print(side_set)


def find_mainList(aim_list):
    # 存储主链路
    mian_list = []
    for item in aim_list:
        if '#' not in item: mian_list.append(item)
    return mian_list


def find_sideList(aim_list):
    # 存储主链路
    side_list = []
    for item in aim_list:
        if '#' in item: side_list.append(item.replace('#', ''))
    return side_list


def find_main(graph, result, end_flag):
    # todo len(result) - 2 的问题 1 3 2 成环的问题
    for i in range(0, len(result) - 1):
        if result[i] != end_flag:
            if result[i] in graph[result[i + 1]]:
                continue
            result[i] = '#' + result[i]
            # 找相连的原子
            for j in range(0, i - 1):
                if result[i - 1 - j] in graph[result[i + 1]]:
                    break
                    # result.remove(result[i - 1])
                result[i - 1 - j] = '#' + result[i - 1 - j]
        else:
            # 将列表后面的元素全部删除
            end_index = result.index(end_flag)
            result[end_index + 1:] = ['#' + item for item in result[end_index + 1:]]
            break
    return result



def DFS(graph, start):
    stack = []
    # 存储序列
    result = []
    # 存储已经访问过的节点
    seen = []
    stack.append(start)
    seen.append(start)
    while stack:
        node = stack.pop()
        neighbors = graph[node]
        # 查看每个相邻的节点
        for neighbor in neighbors:
            if neighbor not in seen:
                stack.append(neighbor)
                seen.append(neighbor)
        # print(node)
        result.append(node)
    return result


if __name__ == "__main__":
    graph = exchange_graph(graph=graph)
    result = DFS(graph, '1')
    print('深度优先序列：', result)
    print('*******************************************************')
    result = DFS(graph, '1')
    final_result = find_main(graph=graph, result=result, end_flag='143')
    print('主侧链连接关系：', final_result)
    mainList = find_mainList(aim_list=final_result)
    print('主链路：', mainList)
    sideList = find_sideList(aim_list=final_result)
    print('侧边链路：', sideList)
    side_set_list = find_side(graph=graph, result=final_result)
    print('侧链集合：', side_set_list)
    final_side = get_final_side(side_set_list=side_set_list)
    print('升序侧链集合：', final_side)
    # 将长度记录下来，相同长度的放在一个列表里面
    index_list = [len(i) for i in final_side]
    print('index_list', index_list)
    flag_index = get_traverse_list(index_list=index_list)
    side_set_list, erased_dic, main_list, graph = find_side_path(graph=graph, side_set_list=final_side,
                                                                 main_list=mainList, sideList=sideList,
                                                                 flag_index=flag_index)
    print('结果：\n')
    print('side_set_list结果：\n', side_set_list)
    print('erased_dic结果：\n', erased_dic)
    print('graph结果：\n', graph)
    print('\nSMILES结果：', main_list)
    time.sleep(0)