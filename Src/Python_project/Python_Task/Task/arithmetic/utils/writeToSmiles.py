# auth: code_king
# time: 2022/11/9 13:24
# file: writeToSmiles.py
import copy


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
def find_side(graph=None, result=None):
    """
    :param graph:
    :param result: 深度遍历的序列
    :return: 侧链集合
    """
    # 存储所有侧链的原子
    side_list = []
    # 存储所有侧链的集合列表
    side_set_list = []
    # 找到'#'的侧链
    for item in result:
        if '#' in item:
            item = item.replace("#", "")
            side_list.append(item)
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
            # 如果前面的原子和最后一个原子不相连，只需要加一下这个原子就行
            if len(temp_set_list) == 0:
                temp_set_list.append(side_list[index])
            side_set_list.append(temp_set_list)
            return side_set_list
            # 最后一个原子需要再判断一下,如果前面一个没有和最后这个原子连续，则最后的原子单独成一个集合
            # if side_list[index] not in side_set_list:
            #     side_set_list.append([side_list[index]])
            # return side_set_list


def find_side_list(graph=None, original_side_list=None):
    """
    :param graph: 无环图
    :param original_side_list: 侧链的序列
    :return: side_set_list（侧链的集合）
    """
    # 存储所有侧链的集合列表
    side_set_list = []
    temp_set_list = []
    # 找侧链的集合列表
    for index in range(0, len(original_side_list)):
        if index != len(original_side_list) - 1:
            # 没进去的话，先进一个
            if original_side_list[index] not in temp_set_list:
                temp_set_list.append(original_side_list[index])
            # 找相邻的两个原子是否有直接连接关系，有则放一起
            if original_side_list[index] in graph[original_side_list[index + 1]]:
                temp_set_list.append(original_side_list[index + 1])
            else:
                side_set_list.append(temp_set_list)
                temp_set_list = []
        else:
            # 如果前面的原子和最后一个原子不相连，只需要加一下这个原子就行
            if len(temp_set_list) == 0:
                temp_set_list.append(original_side_list[index])
            side_set_list.append(temp_set_list)
            return side_set_list


def find_mainList(aim_list):
    # 存储主链路
    mian_list = []
    for item in aim_list:
        if '#' not in item:
            mian_list.append(item)
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


def get_insert_main_atom(insert_atom=None):
    """
    :param insert_atom: 插入的列表
    :return: 插入的列表的主原子长度
    """
    stack = []
    for i in insert_atom:
        if i == ')':
            if i == '(':
                stack.pop()
        else:
            if len(stack) == 0 or stack[-1] != '(':
                stack.append(i)
    return stack


def change_side_main(aim_list=None, end_index=None, end_flag=None):
    global left_side_length, right_side_length, left_start_index, right_end_index
    if end_flag == False:
        stack = []
        for i in range(end_index - 1, -1, -1):
            if aim_list[i] == '(':
                if len(stack) > 0 and stack[-1] == ')':
                    stack.pop()
                else:
                    # 找到起始'('的索引
                    left_start_index = i + 1
                    left_side_length = len(stack)
                    break
            else:
                if i == 0:
                    left_start_index = i
                    left_side_length = len(stack)
                    end_flag = True
                if len(stack) == 0 or stack[-1] != ')':
                    stack.append(aim_list[i])
        stack = []
        for i in range(end_index + 1, len(aim_list)):
            if aim_list[i] == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    right_end_index = i - 1
                    right_side_length = len(stack)
                    break
            else:
                if i == len(aim_list) - 1:
                    right_end_index = i
                    right_side_length = len(stack)
                    end_flag = True
                if len(stack) == 0 or stack[-1] != '(':
                    stack.append(aim_list[i])
        # 判断是否需要改变主链位置
        if left_side_length > right_side_length:
            # 改变主侧位置，先将左边的插入到右边，然后删除左边的原子，再插入右侧的原子
            left_side_list = aim_list[left_start_index:end_index]
            right_side_list = aim_list[end_index + 1:right_end_index + 1]
            # 删除右侧原子
            aim_list = aim_list[:end_index + 1] + aim_list[right_end_index + 1:]
            # 插入右侧
            [aim_list.insert(end_index + 1, left_side_list[i]) for i in range(len(left_side_list) - 1, -1, -1)]
            # 删除左侧原子
            aim_list = aim_list[:left_start_index] + aim_list[end_index:]
            # 插入左侧
            [aim_list.insert(left_start_index, right_side_list[i]) for i in range(len(right_side_list) - 1, -1, -1)]
            # 看看还有没有 右括号 这个地方需要递归
            end_index = right_end_index + 1
            return change_side_main(aim_list=aim_list, end_index=end_index, end_flag=end_flag)
    return aim_list


def side_to_main(insert_index=None, aim_list=None, insert_atom=None):
    """
    用栈的思想很容易可以实现，直接入栈，当匹配到'(',入栈,当栈顶有'(',不让其他元素入栈,如果匹配到')',栈顶有'(',则让它出栈，没有的话结束。
    入栈的时候可以判断栈的数量，如果栈的长度超过插入原子的长度也可以不用跑了，直接当支链插入即可
    :param insert_index: 插入的索引
    :param aim_list: 目标链路
    :param insert_atom: 是一个列表，插入的支链
    :return: aim_list
    """
    stack = []
    end_index = 0
    # 单独计算 insert_atom的主原子个数
    insert_mian_atom = get_insert_main_atom(insert_atom=insert_atom)
    for i in range(insert_index + 1, len(aim_list)):
        if i == len(aim_list) - 1:
            if len(stack) > 0 and stack[-1] != ')' and len(stack) + 1 < len(insert_mian_atom):
                end_index = i + 1
            elif len(stack) + 1 < len(insert_mian_atom):
                end_index = i + 1
        # if i == len(aim_list) - 1 and stack[-1] != ')' and len(stack) + 1 < len(insert_mian_atom):
        #     end_index = i + 1
        if aim_list[i] == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                # 这个是右边括号的索引
                end_index = i
                break
        else:
            if len(stack) == 0 or aim_list[i] == '(' or stack[-1] != '(':
                stack.append(aim_list[i])
                # 优化循环 如果栈里面的原子已经比支链的长度更长，结束循环
                if '(' in stack:
                    if len(stack) - 1 > len(insert_mian_atom):
                        break
                elif len(stack) > len(insert_mian_atom):
                    break
    if end_index == 0:
        # 里面的支链更加长
        insert_atom_index = 1
        aim_list.insert(insert_index + 1, f'(')
        for insert_atom_index in range(1, len(insert_atom) + 1):
            aim_list.insert(insert_index + insert_atom_index + 1, f'{insert_atom[insert_atom_index - 1]}')
        aim_list.insert(insert_index + insert_atom_index + 2, f')')
        # 局部最后括号的索引 56,59,58,55,(,60,57,),47
        # 因为这个是短的，所以并不影响整体
        # end_index = insert_index + insert_atom_index + 2
        # print(aim_list[end_index-1])
    else:
        # 修改面的支链为侧链，外面的支链为主链
        aim_list.insert(insert_index + 1, f'(')
        aim_list.insert(end_index + 1, f')')
        for insert_atom_index in range(1, len(insert_atom) + 1):
            aim_list.insert(end_index + insert_atom_index + 1, f'{insert_atom[insert_atom_index - 1]}')
        # 局部最后括号的索引 (,44,(,45,),46,48,49,50,61,62,63,)
        # 改变支链以后，局部变长，所以外部也需要重新检验 这个是右括号的位置
        # end_index可能有错
        end_index = end_index + 1 + len(insert_atom) + 1
        if end_index < len(aim_list) - 1:
            print(aim_list[end_index])
            # 判断支链变化
            aim_list = change_side_main(aim_list=aim_list, end_index=end_index, end_flag=False)
        else:
            return aim_list
    return aim_list


def insert_aim_list(aim_list=None, aim_atom=None, insert_atom=None):
    """
    :param aim_list: 连接原子的节点
    :param aim_atom: 被插入的原子,是一个列表
    :param insert_atom: 需要去插入的原子
    :return:
    """
    insert_index = aim_list.index(aim_atom)
    if len(insert_atom) == 1:
        # 将当前原子并到主链上去
        aim_list.insert(insert_index + 1, f'(')
        aim_list.insert(insert_index + 2, f'{insert_atom[0]}')
        aim_list.insert(insert_index + 3, f')')
    else:
        # 需要判断这个原子的局部主路原子的长度  如果是3连接1。3,4,5并入 1,6,(,%10,),7。那么考虑6,7,比3,4,5短需要改写成:1,(,6,(,%10,),7,),3,4,5
        aim_list = side_to_main(insert_index=insert_index, aim_list=aim_list, insert_atom=insert_atom)
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
                insert_index = final_side[out_index].index(aim_atom)
                # 需要判断这个原子的局部主路原子的长度  如果是3连接1。3,4,5并入 1,6,(,%10,),7。那么考虑6,7,比3,4,5短需要改写成:1,(,6,(,%10,),7,),3,4,5
                final_side[out_index] = side_to_main(insert_index=insert_index, aim_list=final_side[out_index],
                                                     insert_atom=insert_atom)
            return final_side


def number_to_smiles(unique_link_graph=None, main_list=None, final_side=None):
    # 先将主路赋值给smiles
    smiles_list = copy.deepcopy(main_list)
    for i in range(0, len(final_side)):
        # 注意这个地方是一个列表
        insert_atom = final_side[i]
        aim_atom = unique_link_graph[insert_atom[0]][0]
        # 先找在不在smiles_list上，不在的话再去侧链找。
        if aim_atom in smiles_list:
            insert_aim_list(aim_list=smiles_list, aim_atom=aim_atom, insert_atom=insert_atom)
        else:
            insert_final_side(final_side=final_side, aim_atom=aim_atom, insert_atom=insert_atom)
    return smiles_list
