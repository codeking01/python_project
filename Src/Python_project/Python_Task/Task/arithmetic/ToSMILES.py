import copy
import time

import numpy as np

from Task.arithmetic.utils.smiles_tools import msi_gjf, cyc_6, find_ben_modify_bon, add_element, add_bond, add_bre, \
    get_graph


def exchange_graph(graph=None):
    # 转成字符串
    for i in graph:
        graph[i] = [str(k) for k in graph[i]]

    for i in list(graph.keys()):
        graph[str(i)] = graph[i]
        del graph[i]
    return graph


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


def gen_null_dict(graph_length=None, no_circle_graph=None, unique_link_graph=None):
    for i in range(1, graph_length + 1):
        no_circle_graph[str(i)] = []
    for i in range(1, graph_length + 1):
        unique_link_graph[str(i)] = []
    return no_circle_graph, unique_link_graph


def get_ascend_bradk_graph(bradk_graph=None, smiles_list=None):
    atom_smiles_list = []
    # 只留下原子的smiles
    for item in smiles_list:
        if item != '(' and item != ')':
            atom_smiles_list.append(item)
    smiles_index = {}
    for i in range(1, len(bradk_graph) + 1):
        smiles_index[str(i)] = ''
    # 获取smiles里面所有元素的索引
    for item in atom_smiles_list:
        smiles_index[str(item)] = atom_smiles_list.index(item)


def gen_break_link(bradk_graph=None, smiles=None):
    break_link_graph = {}
    for i in range(1, len(bradk_graph) + 1):
        break_link_graph[str(i)] = []
    for item in smiles:
        if item != ',' and item != '(' and item != ')':
            if len(bradk_graph[str(item)]) != 0:
                # 开始加数字,需要判断里面已经有没有数字
                if len(break_link_graph[str(item)]) != 0:
                    insert_number = int(break_link_graph[str(item)][-1]) + 1
                    # 需要判断数字是否大于10，大于10加 %
                    if insert_number >= 10:
                        insert_number = f'%{insert_number}'
                    break_link_graph[str(item)].append(str(insert_number))
                else:
                    break_link_graph[str(item)].append('1')


def DFS(graph, start):
    # 记录断了环以后的连接关系,先将每个元素对应的列表建立出来,unique_link_graph是父节点
    no_circle_graph, unique_link_graph = gen_null_dict(graph_length=len(graph), no_circle_graph={},
                                                       unique_link_graph={})
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
        final_link_node_index = -1
        # 查看每个相邻的节点
        for neighbor in neighbors:
            if neighbor in result:
                link_node_index = result.index(neighbor)
                if link_node_index > final_link_node_index:
                    final_link_node_index = link_node_index
            if neighbor not in seen:
                stack.append(neighbor)
                seen.append(neighbor)
        if final_link_node_index >= 0:
            no_circle_graph[str(result[final_link_node_index])].append(node)
            no_circle_graph[str(node)].append(result[final_link_node_index])
            unique_link_graph[str(node)].append(result[final_link_node_index])
        result.append(node)
    return result, no_circle_graph, unique_link_graph


def get_degree_zero(no_circle_graph=None):
    """
    :param no_circle_graph: 无环图的连接关系
    :return: 度为1的列表
    """
    zero_list = []
    for i in no_circle_graph:
        if len(no_circle_graph[i]) == 1:
            zero_list.append(i)
    return zero_list


def get_max_road(atom_list=None, no_circle_graph=None, start=None):
    max_road = []
    # for i in range(1, atom_list + 1):
    for i in atom_list:
        result, no_circle_graph, unique_link_graph = DFS(graph=no_circle_graph, start=str(start))
        # print('深度优先序列：', result)
        final_result = find_main(graph=no_circle_graph, result=result, end_flag=f'{i}')
        # print('主侧链连接关系：', final_result)
        main_list = find_mainList(aim_list=final_result)
        # print('主链路：', mainList)
        side_list = find_sideList(aim_list=final_result)
        if len(main_list) > len(max_road):
            max_road = copy.deepcopy(main_list)
            max_final_result = copy.deepcopy(final_result)
            max_main_list = copy.deepcopy(main_list)
            max_side_list = copy.deepcopy(side_list)
        # print('侧边链路：', sideList)
    return max_road, max_final_result, max_main_list, max_side_list


def get_break_graph(graph=None, new_graph=None):
    """
    :param graph: 原来的图
    :param new_graph: 去掉连接关系后的图
    :return: 记录去掉连接关系的图
    """
    break_graph = {}
    for item_index in range(1, len(graph) + 1):
        break_graph[str(item_index)] = list(set(graph[str(item_index)]) - set(new_graph[str(item_index)]))
    # 这个地方是引用传递
    break_graph_keys = []
    for i in break_graph.keys():
        break_graph_keys.append(i)
    for i in break_graph_keys:
        if len(break_graph[i]) == 0:
            del break_graph[i]
    return break_graph


def get_all_max_road(graph=None):
    max_road = []
    for i in range(1, len(graph) + 1):
        # for i in range(3, 4):
        result, no_circle_graph, unique_link_graph = DFS(graph=graph, start=str(i))
        # 只需要找到度为0的就行
        zero_list = get_degree_zero(no_circle_graph=no_circle_graph)
        all_max_road, final_result, main_list, side_list = get_max_road(atom_list=zero_list,
                                                                        no_circle_graph=no_circle_graph, start=str(i))
        if len(all_max_road) > len(max_road):
            max_road = copy.deepcopy(all_max_road)
            max_final_result = copy.deepcopy(final_result)
            max_main_list = copy.deepcopy(main_list)
            max_side_list = copy.deepcopy(side_list)
            max_unique_link_graph = copy.deepcopy(unique_link_graph)
            max_result, max_no_circle_graph = copy.deepcopy(result), copy.deepcopy(no_circle_graph)
            # print('深度优先序列：', result)
            # print('\nNo_Circle_graph：', no_circle_graph)
            # print('*******************************************************')
    return max_road, max_final_result, max_main_list, max_side_list, max_result, max_no_circle_graph, max_unique_link_graph


def insert_aim_list(aim_list=None, aim_atom=None, insert_atom=None):
    """
    :param aim_list: 连接原子的节点
    :param aim_atom: 插入的原子
    :return:
    """
    insert_index = aim_list.index(aim_atom)
    if len(insert_atom) == 1:
        # 将当前原子并到主链上去
        aim_list.insert(insert_index + 1, f'(')
        aim_list.insert(insert_index + 2, f'{insert_atom[0]}')
        aim_list.insert(insert_index + 3, f')')
    else:
        insert_atom_index = 1
        aim_list.insert(insert_index + 1, f'(')
        for insert_atom_index in range(1, len(insert_atom) + 1):
            aim_list.insert(insert_index + insert_atom_index + 1, f'{insert_atom[insert_atom_index - 1]}')
        aim_list.insert(insert_index + insert_atom_index + 2, f')')
    return aim_list


def insert_final_side(final_side=None, aim_atom=None, insert_atom=None):
    """
    :param final_side: 侧链的集合
    :param aim_atom: 要找的连接到的原子
    :param insert_atom: 要插入的原子
    :return: 返回插入好的侧链集合
    """
    # 插入的时候 需要倒着插
    for out_index in range(len(final_side) - 1, -1, -1):
        if aim_atom in final_side[out_index]:
            # 单原子和多原子做法不一样
            if len(insert_atom) == 1:
                final_side[out_index].insert(final_side[out_index].index(aim_atom) + 1, f'(')
                final_side[out_index].insert(final_side[out_index].index(aim_atom) + 2, f'{insert_atom[0]}')
                final_side[out_index].insert(final_side[out_index].index(aim_atom) + 3, f')')
            else:
                insert_index = final_side[out_index].index(aim_atom) + 1
                final_side[out_index].insert(insert_index, f'(')
                for insert_atom_index in range(1, len(insert_atom) + 1):
                    insert_index += 1
                    final_side[out_index].insert(insert_index, f'{insert_atom[insert_atom_index - 1]}')
                final_side[out_index].insert(insert_index + 1, f')')
            return final_side


def gjf_to_smiles(unique_link_graph=None, main_list=None, final_side=None):
    # 先将主路赋值给smiles
    smiles_list = copy.deepcopy(main_list)
    for i in range(0, len(final_side)):
        # 注意这个地方是一个列表
        insert_atom = final_side[i]
        aim_atom = unique_link_graph[insert_atom[0]][0]
        # 先找在不在smiles_list上，不在的话再去侧链找
        if aim_atom in smiles_list:
            insert_aim_list(aim_list=smiles_list, aim_atom=aim_atom, insert_atom=insert_atom)
        else:
            insert_final_side(final_side=final_side, aim_atom=aim_atom, insert_atom=insert_atom)
    return smiles_list


if __name__ == "__main__":
    start = time.time()
    gjf_path = './test/111.gjf'
    MSI_gjf = msi_gjf(gjfpath=gjf_path)
    M_adj = MSI_gjf['M_adj']
    M_S_A = np.array(MSI_gjf['M_S_A'])
    M_S = np.array(MSI_gjf['M_S'])
    M_bon_ = np.array(MSI_gjf['M_bon_'])
    M_atom = MSI_gjf['M_atom']
    n_atom = MSI_gjf['n_atom']
    graph, M_atom_H = get_graph(M_adj=M_adj, M_atom=M_atom)
    sec_graph = copy.deepcopy(graph)
    graph = exchange_graph(graph=graph)
    sec_graph = exchange_graph(graph=sec_graph)
    max_road, final_result, mainList, sideList, result, no_circle_graph, unique_link_graph = get_all_max_road(
        graph=sec_graph)
    print(f'\n***max_road,长度为{len(max_road)}，如下：{max_road}')
    print(f'\n***unique_link_graph:{unique_link_graph}')
    side_set_list = find_side(graph=no_circle_graph, result=final_result)
    print('侧链集合：', side_set_list)
    final_side = get_final_side(side_set_list=side_set_list)
    print('升序侧链集合：', final_side)
    smiles_list = gjf_to_smiles(unique_link_graph=unique_link_graph, main_list=mainList, final_side=final_side)
    print('SMILES:smiles_list：', smiles_list)
    smiles = ','.join(smiles_list)
    print('SMILES:smiles结果：', smiles)
    # temp_list = []
    # for i in smiles_list:
    #     if i != '(' and i != ')':
    #         temp_list.append(i)
    # print('temp_list', temp_list)
    # print('len(temp_list)', len(temp_list))
    break_graph = get_break_graph(graph=graph, new_graph=no_circle_graph)
    print('断掉的连接关系:bradk_graph：', break_graph)
    # 找六元环
    cyc_six = cyc_6(M_S_A=M_S_A, M_S=M_S)
    # 找苯环
    ben_num, cyc_ben, M_bon_1 = find_ben_modify_bon(M_bon_=M_bon_, cyc_six=cyc_six)

    smiles_lst, smiles_atom_lst = add_element(smiles_lst=smiles, M_atom=M_atom, ben_num=ben_num)
    smiles_lst, smiles_atom_lst = add_bond(M_adj=M_adj, M_atom_H=M_atom_H, smiles_lst=smiles_lst,
                                           smiles_atom_lst=smiles_atom_lst, M_atom=M_atom, M_bon_modif=M_bon_1)
    smiles_lst, smiles_atom_lst = add_bre(bre_dic=break_graph, smiles_lst=smiles_lst, smiles_atom_lst=smiles_atom_lst)
    print(''.join(smiles_atom_lst))

    end = time.time()
    print(f'消耗的时间为：{(end - start)}')
