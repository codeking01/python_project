# auth: code_king
# time: 2022/10/19 15:40
# file: testDFS.py

# DFS 为深度优先遍历算法，首先考虑深度，等遍历完深度后再考虑广度
# 出发顶点 start 先入栈，标记为 seen
# 弹出栈顶的一个顶点，将该顶点的相邻未被访问过的顶点 neighbors 入栈，将它们都标记为已访问
# 重复上一步，直到栈空
# 我们可以使用 list 的 pop() 和 append() 充当栈的功能：

# graph = {
#     "A": ["B"],
#     "B": ["A", "C", "G", "K"],
#     "C": ["B", "D", 'M','K'],
#     "D": ["C", "E", "M"],
#     "E": ["D", "F"],
#     "F": ["E"],
#     "G": ["B"],
#     "K": ["B", "M"],
#     "M": ["C", "D", "K"],
# }
# graph = {
#     'A': ['B', 'D', 'C'],
#     'B': ['A', 'P', 'T', 'E'],
#     'C': ['A', 'F'],
#     'D': ['A', 'G', 'Q'],
#     'E': ['B', 'I', 'M'],
#     'F': ['C', 'H'],
#     'G': ['D', 'I', 'L'],
#     'H': ['F', 'I'],
#     'I': ['H', 'G', 'J', 'E', 'Z'],
#     'J': ['I'],
#     'M': ['E', 'N', 'P', 'Z'],
#     'N': ['M', 'P'],
#     'P': ['B', 'M', 'N', 'T'],
#     'L': ['G', 'Q'],
#     'Z': ['I', 'S', 'R', 'M'],
#     'Q': ['D', 'L'],
#     'S': ['Z', 'R'],
#     'R': ['Z', 'S'],
#     'T': ['B', 'P'],
# }
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
def exchange_graph(graph):
    # 转成字符串
    for i in graph:
        graph[i] = [str(k) for k in graph[i]]

    for i in list(graph.keys()):
        graph[str(i)] = graph[i]
        del graph[i]
    return graph


def find_aim_atom(graph_item_list, aim_list):
    '''
    :param graph_item_list:
    :param aim_list: 原子列表(主 侧都行)
    :return: 找到就返回原子，否则返回 ''
    '''
    for graph_item in graph_item_list:
        if graph_item not in aim_list:
            continue
        else:
            # 记录目标原子
            return graph_item
    return ''


def record_atom_link(aim_atom, graph_item_list, erased_dic_list):
    '''
    :param aim_atom: 目标原子，这个原子需要保持连接
    :param graph_item_list: 遍历的连接关系
    :param erased_dic_list: 记录断开的原子
    :return:
    '''
    for graph_item in graph_item_list:
        if graph_item != aim_atom:
            erased_dic_list.append(graph_item)
    return erased_dic_list


def insert_aim_list(aim_list, aim_atom, insert_atom):
    '''
    :param aim_list: 连接原子的节点
    :param aim_atom: 插入的原子
    :return:
    '''
    # 将当前原子并到主链上去
    insert_index = aim_list.index(aim_atom)
    aim_list.insert(insert_index + 1, f'''({insert_atom})''')
    return aim_list


def find_insert_side_index(side_set_list, aim_atom, insert_atom=None):
    '''
    :param side_set_list: 侧链的集合
    :param aim_atom: 要找的连接到的原子
    :param insert_atom: 要插入的原子
    :return: 返回插入好的侧链集合
    '''
    for out_index in range(0, len(side_set_list)):
        if aim_atom in side_set_list[out_index]:
            # side_set_list.insert(side_set_list[out_index].index(aim_atom), f'({insert_atom})')
            side_set_list[out_index].insert(side_set_list[out_index].index(aim_atom) + 1, f'''({insert_atom})''')
            return side_set_list


def del_connection(erased_dic_item_list, graph, del_atom):
    '''
    :param erased_dic_item_list: 要删除的序列
    :param graph: 图
    :param del_atom: 与图绑定的连接起始点
    :return: 处理后的图
    '''
    if len(erased_dic_item_list) != 0:
        for i in erased_dic_item_list:
            graph[i].remove(str(del_atom))
        return graph
    return graph


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
            if start_flag == False :
                flag_index.append([start, end])
    return flag_index

def deal_multiple_atoms(main_list=None,side_set_list=None,flag_index=None):
    for flag_item in flag_index:
        # 单原子之前处理过了，直接跳过即可
        if len(side_set_list[flag_item[0]])==1:
            continue
        else:
            # 处理多个原子的情况 flag_item[1]是列表的后面一个元素，代表结束索引（原序列）,但是我是倒着遍历的，所以是开始索引
            for single_atom_index in range(flag_item[1],flag_item[0]-1,-1):
                # 单集合
                if side_set_list[flag_item[0]]==side_set_list[flag_item[1]]:
                    # 临时记录当前原子 current_item_list代表类似 [1，2，3，4]
                    current_item_list=side_set_list[flag_item[0]]
                    # 先判断是不是在主链上，找到主原子
                    if find_aim_atom(graph_item_list=graph[current_item_list[0]], aim_list=main_list) != '':
                        aim_atom = find_aim_atom(graph_item_list=graph[current_item_list[0]], aim_list=main_list)
                        # 提供graph,
                        for side_item_index in range(len(current_item_list)):
                            # 单独处理头和尾部
                            if side_item_index == 0:
                                root_node = aim_atom
                                next_node = current_item_list[side_item_index + 1]
                                if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                                    continue
                                else:
                                    # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                    for current_node_connection_item in graph[current_item_list[side_item_index]]:
                                        if current_node_connection_item != root_node and current_node_connection_item != next_node:
                                            graph[current_item_list[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(current_item_list[side_item_index])
                            elif side_item_index == len(current_item_list) - 1:
                                pre_node = current_item_list[side_item_index - 1]
                                if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                                    continue
                                else:
                                    for current_node_connection_item in graph[current_item_list[side_item_index]]:
                                        if current_node_connection_item != pre_node:
                                            graph[current_item_list[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(current_item_list[side_item_index])
                            else:
                                pre_node = current_item_list[side_item_index - 1]
                                next_node = current_item_list[side_item_index + 1]
                                if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                                    continue
                                else:
                                    for current_node_connection_item in graph[current_item_list[side_item_index]]:
                                        if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                            graph[current_item_list[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(current_item_list[side_item_index])
                        # 将当前原子并到主链上去
                        main_list = insert_aim_list(aim_list=main_list, aim_atom=aim_atom,
                                                    insert_atom=f'''{str(current_item_list).replace('[', '').replace(']', '')}''')
                    elif find_aim_atom(graph_item_list=graph[current_item_list[0]], aim_list=sideList) != '':
                        # 找上一级侧链连接原子
                        aim_atom = find_aim_atom(graph_item_list=graph[current_item_list[0]], aim_list=sideList)
                        for side_item_index in range(len(current_item_list)):
                            # 单独处理头和尾部
                            if side_item_index == 0:
                                root_node = aim_atom
                                next_node = current_item_list[side_item_index + 1]
                                if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                                    continue
                                else:
                                    # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                    for current_node_connection_item in graph[current_item_list[side_item_index]]:
                                        if current_node_connection_item != root_node and current_node_connection_item != next_node:
                                            graph[current_item_list[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(current_item_list[side_item_index])
                            elif side_item_index == len(current_item_list) - 1:
                                pre_node = current_item_list[side_item_index - 1]
                                if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                                    continue
                                else:
                                    for current_node_connection_item in graph[current_item_list[side_item_index]]:
                                        if current_node_connection_item != pre_node:
                                            graph[current_item_list[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(current_item_list[side_item_index])
                            else:
                                pre_node = current_item_list[side_item_index - 1]
                                next_node = current_item_list[side_item_index + 1]
                                if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                                    continue
                                else:
                                    for current_node_connection_item in graph[current_item_list[side_item_index]]:
                                        if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                            graph[current_item_list[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(current_item_list[side_item_index])
                        # 将当前原子并到侧链链上去
                        side_set_list = find_insert_side_index(side_set_list=side_set_list, aim_atom=aim_atom,
                                                               insert_atom=f'''{str(current_item_list)}''')
                    else:
                        # 判断尾部的原子
                        aim_atom = find_aim_atom(graph_item_list=graph[current_item_list[-1]], aim_list=main_list)
                        # 判断是否主链
                        if aim_atom != '':
                            # 提供graph,
                            for side_item_index in range(len(current_item_list)):
                                # 单独处理头和尾部
                                if side_item_index == 0:
                                    next_node = current_item_list[side_item_index + 1]
                                    if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                                        continue
                                    else:
                                        for current_node_connection_item in graph[current_item_list[side_item_index]]:
                                            if current_node_connection_item != next_node:
                                                graph[current_item_list[side_item_index]].remove(current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(current_item_list[side_item_index])
                                elif side_item_index == len(current_item_list) - 1:
                                    root_node = aim_atom
                                    pre_node = current_item_list[side_item_index - 1]
                                    if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                                        continue
                                    else:
                                        # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                        for current_node_connection_item in graph[current_item_list[side_item_index]]:
                                            if current_node_connection_item != root_node and current_node_connection_item != pre_node:
                                                graph[current_item_list[side_item_index]].remove(current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(current_item_list[side_item_index])
                                else:
                                    pre_node = current_item_list[side_item_index - 1]
                                    next_node = current_item_list[side_item_index + 1]
                                    if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                                        continue
                                    else:
                                        for current_node_connection_item in graph[current_item_list[side_item_index]]:
                                            if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                                graph[current_item_list[side_item_index]].remove(current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(current_item_list[side_item_index])
                            # 将当前原子并到侧边链上去,先将目标原子找到(找到所在的集合)，然后并上去
                            erased_dic[str(current_item_list[-1])] = record_atom_link(aim_atom=aim_atom,
                                                                              graph_item_list=graph[current_item_list[-1]],
                                                                              erased_dic_list=[])
                            side_set_list = find_insert_side_index(side_set_list=side_set_list, aim_atom=aim_atom,
                                                                   insert_atom=f'''{str(current_item_list)}''')
                        else:
                            # 找上一级侧链连接原子
                            aim_atom = find_aim_atom(graph_item_list=graph[current_item_list[-1]], aim_list=sideList)
                            # 提供graph,
                            for side_item_index in range(len(current_item_list)):
                                # 单独处理头和尾部
                                if side_item_index == 0:
                                    next_node = current_item_list[side_item_index + 1]
                                    if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                                        continue
                                    else:
                                        for current_node_connection_item in graph[current_item_list[side_item_index]]:
                                            if current_node_connection_item != next_node:
                                                graph[current_item_list[side_item_index]].remove(current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(current_item_list[side_item_index])
                                elif side_item_index == len(current_item_list) - 1:
                                    root_node = aim_atom
                                    pre_node = current_item_list[side_item_index - 1]
                                    if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                                        continue
                                    else:
                                        # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                        for current_node_connection_item in graph[current_item_list[side_item_index]]:
                                            if current_node_connection_item != root_node and current_node_connection_item != pre_node:
                                                graph[current_item_list[side_item_index]].remove(current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(current_item_list[side_item_index])
                                else:
                                    pre_node = current_item_list[side_item_index - 1]
                                    next_node = current_item_list[side_item_index + 1]
                                    if '(' in current_item_list[side_item_index] or ')' in current_item_list[side_item_index]:
                                        continue
                                    else:
                                        for current_node_connection_item in graph[current_item_list[side_item_index]]:
                                            if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                                graph[current_item_list[side_item_index]].remove(current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(current_item_list[side_item_index])
                            # 将当前原子并到侧边链上去,先将目标原子找到(找到所在的集合)，然后并上去
                            erased_dic[str(current_item_list[-1])] = record_atom_link(aim_atom=aim_atom,
                                                                              graph_item_list=graph[current_item_list[-1]],
                                                                              erased_dic_list=[])
                            side_set_list = find_insert_side_index(side_set_list=side_set_list, aim_atom=aim_atom,
                                                                   insert_atom=f'''({str(current_item_list).replace('[', '').replace(']', '')})''')
                        print('***', current_item_list)
                # 将等长的侧链集合单独处理，

                print(side_set_list[single_atom_index])



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

                # 将等长的侧链集合单独处理，
                # 记录多个相同的侧链集合列表
                temp_list = []
                temp_list.append(side_set_list[item_index])
                # 这一步会决定下次遍历的索引
                for i in range(item_index + 1, len(side_set_list)):
                    if len(side_set_list[item_index]) < len(side_set_list[i]):
                        item_index = i
                        break
                    else:
                        item_index += 1
                        temp_list.append(side_set_list[i])

                # todo 处理单个集合的情况
                if len(temp_list) == 1:
                    # 先判断是不是在主链上，找到主原子
                    if find_aim_atom(graph_item_list=graph[temp_list[0]], aim_list=main_list) != '':
                        aim_atom = find_aim_atom(graph_item_list=graph[item[0]], aim_list=main_list)
                        # 提供graph,
                        for side_item_index in range(len(item)):
                            # 单独处理头和尾部
                            if side_item_index == 0:
                                root_node = aim_atom
                                next_node = item[side_item_index + 1]
                                if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                    continue
                                else:
                                    # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                    for current_node_connection_item in graph[item[side_item_index]]:
                                        if current_node_connection_item != root_node and current_node_connection_item != next_node:
                                            graph[item[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(item[side_item_index])
                            elif side_item_index == len(item) - 1:
                                pre_node = item[side_item_index - 1]
                                if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                    continue
                                else:
                                    for current_node_connection_item in graph[item[side_item_index]]:
                                        if current_node_connection_item != pre_node:
                                            graph[item[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(item[side_item_index])
                            else:
                                pre_node = item[side_item_index - 1]
                                next_node = item[side_item_index + 1]
                                if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                    continue
                                else:
                                    for current_node_connection_item in graph[item[side_item_index]]:
                                        if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                            graph[item[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(item[side_item_index])
                        # 将当前原子并到主链上去
                        main_list = insert_aim_list(aim_list=main_list, aim_atom=aim_atom,
                                                    insert_atom=f'''{str(item).replace('[', '').replace(']', '')}''')
                    elif find_aim_atom(graph_item_list=graph[temp_list[0]], aim_list=sideList) != '':
                        # 找上一级侧链连接原子
                        aim_atom = find_aim_atom(graph_item_list=graph[temp_list[0]], aim_list=sideList)
                        for side_item_index in range(len(temp_list)):
                            # 单独处理头和尾部
                            if side_item_index == 0:
                                root_node = aim_atom
                                next_node = temp_list[side_item_index + 1]
                                if '(' in temp_list[side_item_index] or ')' in temp_list[side_item_index]:
                                    continue
                                else:
                                    # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                    for current_node_connection_item in graph[temp_list[side_item_index]]:
                                        if current_node_connection_item != root_node and current_node_connection_item != next_node:
                                            graph[temp_list[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(temp_list[side_item_index])
                            elif side_item_index == len(temp_list) - 1:
                                pre_node = temp_list[side_item_index - 1]
                                if '(' in temp_list[side_item_index] or ')' in temp_list[side_item_index]:
                                    continue
                                else:
                                    for current_node_connection_item in graph[temp_list[side_item_index]]:
                                        if current_node_connection_item != pre_node:
                                            graph[temp_list[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(temp_list[side_item_index])
                            else:
                                pre_node = temp_list[side_item_index - 1]
                                next_node = temp_list[side_item_index + 1]
                                if '(' in temp_list[side_item_index] or ')' in temp_list[side_item_index]:
                                    continue
                                else:
                                    for current_node_connection_item in graph[temp_list[side_item_index]]:
                                        if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                            graph[temp_list[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(temp_list[side_item_index])
                        # 将当前原子并到侧链链上去
                        side_set_list = find_insert_side_index(side_set_list=side_set_list, aim_atom=aim_atom,
                                                               insert_atom=f'''{str(temp_list)}''')
                    else:
                        # 判断尾部的原子
                        aim_atom = find_aim_atom(graph_item_list=graph[temp_list[-1]], aim_list=main_list)
                        # 判断是否主链
                        if aim_atom != '':
                            # 提供graph,
                            for side_item_index in range(len(temp_list)):
                                # 单独处理头和尾部
                                if side_item_index == 0:
                                    next_node = temp_list[side_item_index + 1]
                                    if '(' in temp_list[side_item_index] or ')' in temp_list[side_item_index]:
                                        continue
                                    else:
                                        for current_node_connection_item in graph[temp_list[side_item_index]]:
                                            if current_node_connection_item != next_node:
                                                graph[temp_list[side_item_index]].remove(current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(temp_list[side_item_index])
                                elif side_item_index == len(temp_list) - 1:
                                    root_node = aim_atom
                                    pre_node = temp_list[side_item_index - 1]
                                    if '(' in temp_list[side_item_index] or ')' in temp_list[side_item_index]:
                                        continue
                                    else:
                                        # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                        for current_node_connection_item in graph[temp_list[side_item_index]]:
                                            if current_node_connection_item != root_node and current_node_connection_item != pre_node:
                                                graph[temp_list[side_item_index]].remove(current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(temp_list[side_item_index])
                                else:
                                    pre_node = temp_list[side_item_index - 1]
                                    next_node = temp_list[side_item_index + 1]
                                    if '(' in temp_list[side_item_index] or ')' in temp_list[side_item_index]:
                                        continue
                                    else:
                                        for current_node_connection_item in graph[temp_list[side_item_index]]:
                                            if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                                graph[temp_list[side_item_index]].remove(current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(temp_list[side_item_index])
                            # 将当前原子并到侧边链上去,先将目标原子找到(找到所在的集合)，然后并上去
                            erased_dic[str(temp_list[-1])] = record_atom_link(aim_atom=aim_atom,
                                                                              graph_item_list=graph[temp_list[-1]],
                                                                              erased_dic_list=[])
                            side_set_list = find_insert_side_index(side_set_list=side_set_list, aim_atom=aim_atom,
                                                                   insert_atom=f'''{str(temp_list)}''')
                        else:
                            # 找上一级侧链连接原子
                            aim_atom = find_aim_atom(graph_item_list=graph[temp_list[-1]], aim_list=sideList)
                            # 提供graph,
                            for side_item_index in range(len(temp_list)):
                                # 单独处理头和尾部
                                if side_item_index == 0:
                                    next_node = temp_list[side_item_index + 1]
                                    if '(' in temp_list[side_item_index] or ')' in temp_list[side_item_index]:
                                        continue
                                    else:
                                        for current_node_connection_item in graph[temp_list[side_item_index]]:
                                            if current_node_connection_item != next_node:
                                                graph[temp_list[side_item_index]].remove(current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(temp_list[side_item_index])
                                elif side_item_index == len(temp_list) - 1:
                                    root_node = aim_atom
                                    pre_node = temp_list[side_item_index - 1]
                                    if '(' in temp_list[side_item_index] or ')' in temp_list[side_item_index]:
                                        continue
                                    else:
                                        # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                        for current_node_connection_item in graph[temp_list[side_item_index]]:
                                            if current_node_connection_item != root_node and current_node_connection_item != pre_node:
                                                graph[temp_list[side_item_index]].remove(current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(temp_list[side_item_index])
                                else:
                                    pre_node = temp_list[side_item_index - 1]
                                    next_node = temp_list[side_item_index + 1]
                                    if '(' in temp_list[side_item_index] or ')' in temp_list[side_item_index]:
                                        continue
                                    else:
                                        for current_node_connection_item in graph[temp_list[side_item_index]]:
                                            if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                                graph[temp_list[side_item_index]].remove(current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(temp_list[side_item_index])
                            # 将当前原子并到侧边链上去,先将目标原子找到(找到所在的集合)，然后并上去
                            erased_dic[str(temp_list[-1])] = record_atom_link(aim_atom=aim_atom,
                                                                              graph_item_list=graph[temp_list[-1]],
                                                                              erased_dic_list=[])
                            side_set_list = find_insert_side_index(side_set_list=side_set_list, aim_atom=aim_atom,
                                                                   insert_atom=f'''({str(temp_list).replace('[', '').replace(']', '')})''')
                        print('***', temp_list)
                else:
                    # todo 处理等长的侧链集合单独处理,需要从后面往前面处理
                    for temp_list_index in range(len(temp_list) - 1, -1, -1):
                        # 要么并到主链上，要么并到前面的侧链路上 如[[2,3],[5,6],[7,8],[9,10]]，[9,10]要么并到主路，要不就并到前面的[2,3]等
                        # 先找主路
                        if find_aim_atom(graph_item_list=graph[temp_list[temp_list_index][0]],
                                         aim_list=main_list) != '':
                            aim_atom = find_aim_atom(graph_item_list=graph[temp_list[temp_list_index][0]],
                                                     aim_list=main_list)
                            # 提供graph,
                            for side_item_index in range(len(temp_list[temp_list_index])):
                                # 单独处理头和尾部
                                if side_item_index == 0:
                                    root_node = aim_atom
                                    next_node = temp_list[temp_list_index][side_item_index + 1]
                                    if '(' in temp_list[temp_list_index][side_item_index] or ')' in \
                                            temp_list[temp_list_index][side_item_index]:
                                        continue
                                    else:
                                        # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                        for current_node_connection_item in graph[
                                            temp_list[temp_list_index][side_item_index]]:
                                            if current_node_connection_item != root_node and current_node_connection_item != next_node:
                                                graph[temp_list[temp_list_index][side_item_index]].remove(
                                                    current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(
                                                    temp_list[temp_list_index][side_item_index])
                                elif side_item_index == len(temp_list[temp_list_index]) - 1:
                                    pre_node = temp_list[temp_list_index][side_item_index - 1]
                                    if '(' in temp_list[temp_list_index][side_item_index] or ')' in \
                                            temp_list[temp_list_index][side_item_index]:
                                        continue
                                    else:
                                        for current_node_connection_item in graph[
                                            temp_list[temp_list_index][side_item_index]]:
                                            if current_node_connection_item != pre_node:
                                                graph[temp_list[temp_list_index][side_item_index]].remove(
                                                    current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(
                                                    temp_list[temp_list_index][side_item_index])
                                else:
                                    pre_node = temp_list[temp_list_index][side_item_index - 1]
                                    next_node = temp_list[temp_list_index][side_item_index + 1]
                                    if '(' in temp_list[temp_list_index][side_item_index] or ')' in \
                                            temp_list[temp_list_index][side_item_index]:
                                        continue
                                    else:
                                        for current_node_connection_item in graph[
                                            temp_list[temp_list_index][side_item_index]]:
                                            if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                                graph[temp_list[temp_list_index][side_item_index]].remove(
                                                    current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(
                                                    temp_list[temp_list_index][side_item_index])
                            # 将当前原子并到主链上去
                            main_list = insert_aim_list(aim_list=main_list, aim_atom=aim_atom,
                                                        insert_atom=f'''{str(temp_list[temp_list_index]).replace('[', '').replace(']', '')}''')
                        elif find_aim_atom(graph_item_list=graph[temp_list[temp_list_index][-1]],
                                           aim_list=main_list) != '':
                            # 判断尾部的原子
                            aim_atom = find_aim_atom(graph_item_list=graph[temp_list[temp_list_index][-1]],
                                                     aim_list=main_list)
                            # 判断是否主链
                            # 提供graph,
                            for side_item_index in range(len(temp_list[temp_list_index])):
                                # 单独处理头和尾部
                                if side_item_index == 0:
                                    next_node = temp_list[temp_list_index][side_item_index + 1]
                                    if '(' in temp_list[temp_list_index][side_item_index] or ')' in \
                                            temp_list[temp_list_index][side_item_index]:
                                        continue
                                    else:
                                        for current_node_connection_item in graph[
                                            temp_list[temp_list_index][side_item_index]]:
                                            if current_node_connection_item != next_node:
                                                graph[temp_list[temp_list_index][side_item_index]].remove(
                                                    current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(
                                                    temp_list[temp_list_index][side_item_index])
                                elif side_item_index == len(temp_list[temp_list_index]) - 1:
                                    root_node = aim_atom
                                    pre_node = temp_list[temp_list_index][side_item_index - 1]
                                    if '(' in temp_list[temp_list_index][side_item_index] or ')' in \
                                            temp_list[temp_list_index][side_item_index]:
                                        continue
                                    else:
                                        # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                        for current_node_connection_item in graph[
                                            temp_list[temp_list_index][side_item_index]]:
                                            if current_node_connection_item != root_node and current_node_connection_item != pre_node:
                                                graph[temp_list[temp_list_index][side_item_index]].remove(
                                                    current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(
                                                    temp_list[temp_list_index][side_item_index])
                                else:
                                    pre_node = temp_list[temp_list_index][side_item_index - 1]
                                    next_node = temp_list[temp_list_index][side_item_index + 1]
                                    if '(' in temp_list[temp_list_index][side_item_index] or ')' in \
                                            temp_list[temp_list_index][side_item_index]:
                                        continue
                                    else:
                                        for current_node_connection_item in graph[
                                            temp_list[temp_list_index][side_item_index]]:
                                            if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                                graph[temp_list[temp_list_index][side_item_index]].remove(
                                                    current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(
                                                    temp_list[temp_list_index][side_item_index])
                            # 将当前原子并到侧边链上去,先将目标原子找到(找到所在的集合)，然后并上去
                            erased_dic[str(temp_list[temp_list_index][-1])] = record_atom_link(aim_atom=aim_atom,
                                                                                               graph_item_list=graph[
                                                                                                   temp_list[
                                                                                                       temp_list_index][
                                                                                                       -1]],
                                                                                               erased_dic_list=[])
                            side_set_list = find_insert_side_index(side_set_list=side_set_list, aim_atom=aim_atom,
                                                                   insert_atom=f'''{str(temp_list[temp_list_index])}''')
                        # 去找侧链的
                        else:
                            # 找侧链，然后并到前面的侧链上
                            # 将这个同大小的侧链集合的头尾原子全部取出来放到一个列表，用来遍历
                            same_side_list = []
                            for temp_list_preIndex in range(0, temp_list_index):
                                same_side_list.append(temp_list[temp_list_preIndex][0])
                                same_side_list.append(temp_list[temp_list_preIndex][-1])

                            # if find_aim_atom(graph_item_list=graph[temp_list[temp_list_index][0]],
                            #                  aim_list=same_side_list) != '':
                            # 找上一级侧链连接原子
                            aim_atom = find_aim_atom(graph_item_list=graph[temp_list[temp_list_index][0]],
                                                     aim_list=same_side_list)
                            for side_item_index in range(len(temp_list[temp_list_index])):
                                # 单独处理头和尾部
                                if side_item_index == 0:
                                    root_node = aim_atom
                                    next_node = temp_list[temp_list_index][side_item_index + 1]
                                    if '(' in temp_list[temp_list_index][side_item_index] or ')' in \
                                            temp_list[temp_list_index][side_item_index]:
                                        continue
                                    else:
                                        # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                        for current_node_connection_item in graph[
                                            temp_list[temp_list_index][side_item_index]]:
                                            if current_node_connection_item != root_node and current_node_connection_item != next_node:
                                                graph[temp_list[temp_list_index][side_item_index]].remove(
                                                    current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(
                                                    temp_list[temp_list_index][side_item_index])
                                elif side_item_index == len(temp_list[temp_list_index]) - 1:
                                    pre_node = temp_list[temp_list_index][side_item_index - 1]
                                    if '(' in temp_list[temp_list_index][side_item_index] or ')' in \
                                            temp_list[temp_list_index][side_item_index]:
                                        continue
                                    else:
                                        for current_node_connection_item in graph[
                                            temp_list[temp_list_index][side_item_index]]:
                                            if current_node_connection_item != pre_node:
                                                graph[temp_list[temp_list_index][side_item_index]].remove(
                                                    current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(
                                                    temp_list[temp_list_index][side_item_index])
                                else:
                                    pre_node = temp_list[temp_list_index][side_item_index - 1]
                                    next_node = temp_list[temp_list_index][side_item_index + 1]
                                    if '(' in temp_list[temp_list_index][side_item_index] or ')' in \
                                            temp_list[temp_list_index][side_item_index]:
                                        continue
                                    else:
                                        for current_node_connection_item in graph[
                                            temp_list[temp_list_index][side_item_index]]:
                                            if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                                graph[temp_list[temp_list_index][side_item_index]].remove(
                                                    current_node_connection_item)
                                                # 同时删除其他原子与当前原子的连接关系
                                                graph[current_node_connection_item].remove(
                                                    temp_list[temp_list_index][side_item_index])
                            # 将当前原子并到侧链链上去
                            side_set_list = find_insert_side_index(side_set_list=side_set_list,
                                                                   aim_atom=aim_atom,
                                                                   insert_atom=f'''{str(temp_list[temp_list_index])}''')

                # todo:删除--
                # 先判断是不是在主链上，找到主原子
                if find_aim_atom(graph_item_list=graph[item[0]], aim_list=main_list) != '':
                    aim_atom = find_aim_atom(graph_item_list=graph[item[0]], aim_list=main_list)
                    # 提供graph,
                    for side_item_index in range(len(item)):
                        # 单独处理头和尾部
                        if side_item_index == 0:
                            root_node = aim_atom
                            next_node = item[side_item_index + 1]
                            if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                continue
                            else:
                                # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                for current_node_connection_item in graph[item[side_item_index]]:
                                    if current_node_connection_item != root_node and current_node_connection_item != next_node:
                                        graph[item[side_item_index]].remove(current_node_connection_item)
                                        # 同时删除其他原子与当前原子的连接关系
                                        graph[current_node_connection_item].remove(item[side_item_index])
                        elif side_item_index == len(item) - 1:
                            pre_node = item[side_item_index - 1]
                            if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                continue
                            else:
                                for current_node_connection_item in graph[item[side_item_index]]:
                                    if current_node_connection_item != pre_node:
                                        graph[item[side_item_index]].remove(current_node_connection_item)
                                        # 同时删除其他原子与当前原子的连接关系
                                        graph[current_node_connection_item].remove(item[side_item_index])
                        else:
                            pre_node = item[side_item_index - 1]
                            next_node = item[side_item_index + 1]
                            if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                continue
                            else:
                                for current_node_connection_item in graph[item[side_item_index]]:
                                    if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                        graph[item[side_item_index]].remove(current_node_connection_item)
                                        # 同时删除其他原子与当前原子的连接关系
                                        graph[current_node_connection_item].remove(item[side_item_index])
                    # 将当前原子并到主链上去
                    main_list = insert_aim_list(aim_list=main_list, aim_atom=aim_atom,
                                                insert_atom=f'''{str(item).replace('[', '').replace(']', '')}''')
                elif find_aim_atom(graph_item_list=graph[item[0]], aim_list=sideList) != '':
                    # 找上一级侧链连接原子
                    aim_atom = find_aim_atom(graph_item_list=graph[item[0]], aim_list=sideList)
                    # ***
                    for side_item_index in range(len(item)):
                        # 单独处理头和尾部
                        if side_item_index == 0:
                            root_node = aim_atom
                            next_node = item[side_item_index + 1]
                            if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                continue
                            else:
                                # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                for current_node_connection_item in graph[item[side_item_index]]:
                                    if current_node_connection_item != root_node and current_node_connection_item != next_node:
                                        graph[item[side_item_index]].remove(current_node_connection_item)
                                        # 同时删除其他原子与当前原子的连接关系
                                        graph[current_node_connection_item].remove(item[side_item_index])
                        elif side_item_index == len(item) - 1:
                            pre_node = item[side_item_index - 1]
                            if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                continue
                            else:
                                for current_node_connection_item in graph[item[side_item_index]]:
                                    if current_node_connection_item != pre_node:
                                        graph[item[side_item_index]].remove(current_node_connection_item)
                                        # 同时删除其他原子与当前原子的连接关系
                                        graph[current_node_connection_item].remove(item[side_item_index])
                        else:
                            pre_node = item[side_item_index - 1]
                            next_node = item[side_item_index + 1]
                            if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                continue
                            else:
                                for current_node_connection_item in graph[item[side_item_index]]:
                                    if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                        graph[item[side_item_index]].remove(current_node_connection_item)
                                        # 同时删除其他原子与当前原子的连接关系
                                        graph[current_node_connection_item].remove(item[side_item_index])
                    # 将当前原子并到侧链链上去
                    side_set_list = find_insert_side_index(side_set_list=side_set_list, aim_atom=aim_atom,
                                                           insert_atom=f'''{str(item)}''')
                else:
                    # 判断尾部的原子
                    aim_atom = find_aim_atom(graph_item_list=graph[item[-1]], aim_list=main_list)
                    # 判断是否主链
                    if aim_atom != '':
                        # 提供graph,
                        for side_item_index in range(len(item)):
                            # 单独处理头和尾部
                            if side_item_index == 0:
                                next_node = item[side_item_index + 1]
                                if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                    continue
                                else:
                                    for current_node_connection_item in graph[item[side_item_index]]:
                                        if current_node_connection_item != next_node:
                                            graph[item[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(item[side_item_index])
                            elif side_item_index == len(item) - 1:
                                root_node = aim_atom
                                pre_node = item[side_item_index - 1]
                                if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                    continue
                                else:
                                    # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                    for current_node_connection_item in graph[item[side_item_index]]:
                                        if current_node_connection_item != root_node and current_node_connection_item != pre_node:
                                            graph[item[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(item[side_item_index])
                            else:
                                pre_node = item[side_item_index - 1]
                                next_node = item[side_item_index + 1]
                                if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                    continue
                                else:
                                    for current_node_connection_item in graph[item[side_item_index]]:
                                        if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                            graph[item[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(item[side_item_index])
                        # 将当前原子并到侧边链上去,先将目标原子找到(找到所在的集合)，然后并上去
                        erased_dic[str(item[-1])] = record_atom_link(aim_atom=aim_atom, graph_item_list=graph[item[-1]],
                                                                     erased_dic_list=[])
                        side_set_list = find_insert_side_index(side_set_list=side_set_list, aim_atom=aim_atom,
                                                               insert_atom=f'''{str(item)}''')
                    else:
                        # 找上一级侧链连接原子
                        aim_atom = find_aim_atom(graph_item_list=graph[item[-1]], aim_list=sideList)
                        # 提供graph,
                        for side_item_index in range(len(item)):
                            # 单独处理头和尾部
                            if side_item_index == 0:
                                next_node = item[side_item_index + 1]
                                if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                    continue
                                else:
                                    for current_node_connection_item in graph[item[side_item_index]]:
                                        if current_node_connection_item != next_node:
                                            graph[item[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(item[side_item_index])
                            elif side_item_index == len(item) - 1:
                                root_node = aim_atom
                                pre_node = item[side_item_index - 1]
                                if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                    continue
                                else:
                                    # 遍历当前节点所有连接关系，除了上面这两个不删除，其他的都删除
                                    for current_node_connection_item in graph[item[side_item_index]]:
                                        if current_node_connection_item != root_node and current_node_connection_item != pre_node:
                                            graph[item[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(item[side_item_index])
                            else:
                                pre_node = item[side_item_index - 1]
                                next_node = item[side_item_index + 1]
                                if '(' in item[side_item_index] or ')' in item[side_item_index]:
                                    continue
                                else:
                                    for current_node_connection_item in graph[item[side_item_index]]:
                                        if current_node_connection_item != pre_node and current_node_connection_item != next_node:
                                            graph[item[side_item_index]].remove(current_node_connection_item)
                                            # 同时删除其他原子与当前原子的连接关系
                                            graph[current_node_connection_item].remove(item[side_item_index])
                        # 将当前原子并到侧边链上去,先将目标原子找到(找到所在的集合)，然后并上去
                        erased_dic[str(item[-1])] = record_atom_link(aim_atom=aim_atom, graph_item_list=graph[item[-1]],
                                                                     erased_dic_list=[])
                        side_set_list = find_insert_side_index(side_set_list=side_set_list, aim_atom=aim_atom,
                                                               insert_atom=f'''({str(item).replace('[', '').replace(']', '')})''')
                # TODO:删除--

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
    for i in range(0, len(result) - 2):
        if result[i] != end_flag:
            if result[i] in graph[result[i + 1]]:
                continue
            # result.remove(result[i])
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
            # result = result[:end_index + 1]
            # result = result.remove('#)
            # break
            # result[end_index+1:]='#'
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
