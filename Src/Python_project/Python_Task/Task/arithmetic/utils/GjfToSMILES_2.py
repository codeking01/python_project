import copy
import itertools
import re
import time

import numpy as np
from numpy import mat, inf

from Task.arithmetic.ToSMILES import exchange_graph, gjf_to_smiles, find_side, get_final_side, get_break_graph
from Task.arithmetic.utils.smiles_tools import get_max_road, get_degree_zero, code_king_DFS

elements_table = {
    'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10,
    'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20,
    'Sc': 21, 'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25, 'Fe': 26, 'Co': 27, 'Ni': 28, 'Cu': 29, 'Zn': 30,
    'Ga': 31, 'Ge': 32, 'As': 33, 'Se': 34, 'Br': 35, 'Kr': 36, 'Rb': 37, 'Sr': 38, 'Y': 39, 'Zr': 40,
    'Nb': 41, 'Mo': 42, 'Tc': 43, 'Ru': 44, 'Rh': 45, 'Pd': 46, 'Ag': 47, 'Cd': 48, 'In': 49, 'Sn': 50,
    'Sb': 51, 'Te': 52, 'I': 53, 'Xe': 54, 'Cs': 55, 'Ba': 56, 'La': 57, 'Ce': 58, 'Pr': 59, 'Nd': 60,
    'Pm': 61, 'Sm': 62, 'Eu': 63, 'Gd': 64, 'Tb': 65, 'Dy': 66, 'Ho': 67, 'Er': 68, 'Tm': 69, 'Yb': 70,
    'Lu': 71, 'Hf': 72, 'Ta': 73, 'W': 74, 'Re': 75, 'Os': 76, 'Ir': 77, 'Pt': 78, 'Au': 79, 'Hg': 80,
    'TI': 81, 'Pb': 82, 'Bi': 83, 'Po': 84, 'At': 85, 'Rn': 86, 'Fr': 87, 'Ra': 88, 'Ac': 89, 'Th': 90,
    'Pa': 91, 'U': 92, 'Np': 93, 'Pu': 94, 'Am': 95, 'Cm': 96, 'Bk': 97, 'Cf': 98, 'Es': 99, 'Fm': 100,
    'Md': 101, 'No': 102, 'Lr': 103, 'Rf': 104, 'Db': 105, 'Sg': 106, 'Bh': 107, 'Hs': 108, 'Mt': 109, 'Ds': 110,
    'Rg': 111, 'Cn': 112, 'Nh': 113, 'Fi': 114, 'Mc': 115, 'Lv': 116, 'Ts': 117, 'Og': 118
}


def m_s(n_atom, M_S_A, M_adj):
    """
    生成步长矩阵
    :param n_atom: 原子数
    :param M_S_A: 相邻矩阵
    :param M_adj: 连接关系，list类型
    :return: M_S: 步长矩阵
    """
    M_S = M_S_A.copy()
    for m in range(1, n_atom - 1):
        w_ms = np.where(M_S == m)
        if len(w_ms[0]) == 0:  # 节省时间
            break
        for i in range(0, len(w_ms[0])):
            w_msi = M_adj[w_ms[1][i]]
            for j in w_msi:
                # M_S[w_ms[0][i],j-1]==0去掉描述过的   w_ms[0][i]!=j-1    去掉自身，保证对角线元素为0
                if M_S[w_ms[0][i], j - 1] == 0 and w_ms[0][i] != (j - 1):
                    M_S[w_ms[0][i], j - 1] = m + 1
                    M_S[j - 1, w_ms[0][i]] = m + 1
    return M_S


def msi_gjf(gjf_path):
    """
    提取 gjf 文件信息
    :param gjfpath: gjf 文件路径
    :return:
    """
    orimsi_o = open(file=gjf_path)
    orimsi_all = orimsi_o.readlines()
    orimsi_o.close()
    M_atom = []
    n_atom = 0
    for i_L in orimsi_all:
        if i_L[5:12] == '       ':
            n_atom = n_atom + 1
            i_L = i_L.replace('\n', '')
            i_L = i_L.split()
            i_at = i_L[0]
            M_atom.append(i_at)
    M_S_A = mat(np.zeros((n_atom, n_atom)))  # 构建一个相邻矩阵
    M_bon_ = mat(np.zeros((n_atom, n_atom)))  # 构建一个键的矩阵
    for i_L in orimsi_all:
        i_L = i_L.split()
        if len(i_L) > 2 and i_L[0].isdigit():
            i_L_n = list(map(float, i_L))  # 数字全部转成  float
            i_L_n_i = np.hstack((i_L_n[0], i_L_n[1::2])) - 1  # 取原子序号，以0为第一个原子
            i_L_n_i = i_L_n_i.astype(np.int64)  # 转类型，float 转 int
            M_S_A[i_L_n_i[0], list(i_L_n_i[1::])] = 1  # 相连原子标1
            M_bon_[i_L_n_i[0], list(i_L_n_i[1::])] = i_L_n[2::2]  # 相连的方式
    M_S_A = M_S_A + M_S_A.T  # 构建实对称矩阵,大于1的改为1
    M_bon_ = M_bon_ + M_bon_.T  # 需要修改
    M_adj_H = []
    M_adj_nH = []
    M_adj = []
    M_bon = []
    for j in range(0, n_atom):
        M_adj_ = np.where(M_S_A[j, :] > 0)
        M_adj.append(list(1 + M_adj_[1]))
        M_bon.append(M_bon_[j, M_adj_[1]].tolist()[0])
        M_adj__ = []  # H
        M_adj_nH_ = []  # 非 H
        for i in M_adj_[1]:
            if M_atom[i] == 'H':
                M_adj__.append(i + 1)
            else:
                M_adj_nH_.append(i + 1)
        M_adj_nH.append(M_adj_nH_)
        M_adj_H.append(M_adj__)
    M_S = m_s(n_atom, M_S_A, M_adj)
    M_aro = mat(np.zeros((n_atom, 1)))
    for k in range(n_atom):
        if len(np.where(mat(M_bon[k]) == 1.5)[1]) > 0:
            M_aro[k, 0] = 1
    M_cyc = mat(np.zeros((n_atom, 1)))
    for i in range(0, n_atom):
        if len(M_adj_nH[i]) > 1:  # 为什么不写大于 1
            for j in range(0, n_atom):
                wl = np.where(M_S[j, (mat(M_adj_nH[i]) - 1).tolist()[0]] < M_S[j, i] + 1)[1]
                if len(wl) > 1:
                    M_cyc[i, 0] = 1
                    break
    MSI = {'n_atom': n_atom, 'M_S_A': M_S_A, 'M_S': M_S, 'M_bon': M_bon, 'M_bon_': M_bon_, 'M_atom': M_atom,
           'M_aro': M_aro, 'M_adj': M_adj, 'M_adj_H': M_adj_H, 'M_adj_nH': M_adj_nH, 'M_cyc': M_cyc}
    return MSI


def get_graph(n_atom_nH, atom_num, connect_H_num, M_S_A_nH, M_bon_2_nH, M_S_nH, M_adj_nH):
    """
    生成 graph,去掉 H 的
    :param n_atom_nH: 非氢原子数
    :param atom_num: 原子序号列表
    :param connect_H_num: 连接氢原子数量
    :param M_S_A_nH: 去氢的相邻矩阵
    :param M_bon_2_nH: 去氢的键值矩阵，苯环类型为 4
    :param M_S_nH: 去氢的步长矩阵
    :param M_adj_nH: 去氢的连接关系
    :return: graph: 去氢的图
    :return: x_atom: 优先级排序
    :return: rank_0: 优先级
    :return: sym: 是否对称
    """
    branch_degree_nH = np.sum(M_S_A_nH, axis=0, dtype=int)
    bond_nH_sum = np.sum(M_bon_2_nH, axis=0, dtype=int)
    all_property = []
    for i in range(len(atom_num)):
        x1 = str(branch_degree_nH[i])
        x2 = str(bond_nH_sum[i]).zfill(2)
        x3 = str(atom_num[i]).zfill(3)
        x4 = str(connect_H_num[i])
        x = x1 + x2 + x3 + x4
        all_property.append(int(x))
    all_property = np.array(all_property)
    rank_0 = sort_1(a=all_property)
    rank_f = list(rank_0)
    rank_f = list(set(rank_f))
    if len(rank_f) == 1:
        k = 2
        max_step = int(np.max(M_S_nH[:, 1]))
        for i in range(1, max_step + 1):
            ss = np.where(M_S_nH[:, 1] == i)[0]
            ss = list(ss)
            for j in range(len(ss)):
                rank_0[ss[j]] = k
                k += 1
        x_index = np.argsort(rank_0)
        index_nH = np.arange(0, n_atom_nH, 1)
        x_atom = index_nH[x_index]
        x_atom = x_atom.tolist()
        x_atom = [i + 1 for i in x_atom]
        graph = {}
        for i in range(len(M_adj_nH)):
            adj_x = M_adj_nH[i]
            adj_x.sort(key=x_atom.index)
            graph[i + 1] = adj_x
        sym = 1
    else:
        prime_table = primes(10000)
        start_flag = -1
        end_flag = 0
        while start_flag != end_flag:
            start_flag = end_flag
            M_cul_0 = copy.deepcopy(M_S_A_nH)
            rank_prime = sort_2(a=rank_0, prime_table=prime_table)
            rank_prime_mult = np.zeros(shape=(n_atom_nH,), dtype=int)
            for i in range(n_atom_nH):
                ss_w = np.where(M_cul_0[i, :] != 0)[0]
                M_cul_0[i, ss_w] = rank_prime[ss_w]
            for i in range(n_atom_nH):
                ss_w = np.where(M_cul_0[i, :] != 0)[0]
                rank_prime_mult[i] = np.prod(M_cul_0[i, ss_w])
            rank_1 = sort_3(a1=rank_0, a2=rank_prime_mult)
            rank_0 = rank_1
            end_flag = len(list(set(rank_0.tolist())))
        x_index = np.argsort(-rank_0)
        index_nH = np.arange(0, n_atom_nH, 1)
        x_atom = index_nH[x_index]
        x_atom = x_atom.tolist()
        x_atom = [i + 1 for i in x_atom]
        graph = {}
        for i in range(len(M_adj_nH)):
            adj_x = M_adj_nH[i]
            adj_x.sort(key=x_atom.index)
            graph[i + 1] = adj_x
        sym = 0
    return graph, x_atom, rank_0, sym


def gen_MS(M_adj, n_atom):
    """
    根据连接关系写出步长矩阵
    :param M_adj: 连接关系
    :param n_atom: 原子数
    :return: 相邻矩阵；步长矩阵
    """
    M_S_A = mat(np.zeros((n_atom, n_atom)))  # 构建一个相邻矩阵
    for i in range(len(M_adj)):
        for j in M_adj[i]:
            M_S_A[i, j - 1] = 1
    MS = m_s(n_atom, M_S_A, M_adj)
    M_S_A = np.array(M_S_A)
    MS = np.array(MS)
    return M_S_A, MS


def BFS(graph, start):
    """
    广度搜索
    :param graph: 图，dict 类型
    :param start: 开始点
    :return:
    """
    result = []
    queue = []  # 定义一个队列
    queue.append(start)  # 将任一个节点放入
    seen = set()  # 建立一个集合，集合就是用来判断该元素是不是已经出现过
    seen.add(start)
    parent = {start: None}
    while (len(queue) > 0):  # 当队里还有东西时
        vertex = queue.pop(0)  # 取出队头元素
        nodes = graph[vertex]  # 查看出入队节点的相邻节点
        for m in nodes:
            if m not in seen:
                queue.append(m)
                seen.add(m)  # 添加到访问过的集合里面
                parent[m] = vertex  # 标记父节点
        result.append(vertex)
    return parent, result


def DFS(graph, start):
    """
    初次深度搜索
    :param graph: 图
    :param start: 起始点
    :return: 广度搜索结果；新的图（断键后的）
    """
    stack = []  # 定义一个栈
    result = []
    seen = []  # 存储已经访问过的节点
    new_graph = {}
    graph_keys = list(graph.keys())
    stack.append(start)
    seen.append(start)
    for i in range(len(graph_keys)):
        new_graph[graph_keys[i]] = []
    while (len(stack) > 0):
        node = stack.pop()  # .pop() 默认移除最后一个元素
        neighbors = graph[node]
        for neighbor in neighbors:  # 查看每个相邻的节点
            if neighbor not in seen:  # 判断邻点没出现过
                stack.append(neighbor)
                seen.append(neighbor)
        for i in range(len(result) - 1, -1, -1):
            if result[i] in neighbors:
                new_graph[node].append(result[i])
                new_graph[result[i]].append(node)
                break
        result.append(node)
    return result, new_graph


def break_bond(graph, new_graph, M_bon_2):
    """
    断键位置
    :param graph: 旧图
    :param new_graph: 新图 无环的
    :return: 断键的字典
    """
    bre_dic = {}
    graph_keys = list(graph.keys())
    M_bon_2_f = copy.deepcopy(M_bon_2)
    for i in range(len(graph)):
        x = list(set(graph[graph_keys[i]]) - set(new_graph[graph_keys[i]]))
        x = [str(j) for j in x]
        if len(x) > 0:
            bre_dic[str(graph_keys[i])] = x
    bre_dic_keys = list(bre_dic.keys())
    bre_dic_values = list(bre_dic.values())
    for i in range(len(bre_dic_keys)):
        x1 = int(bre_dic_keys[i]) - 1
        for j in range(len(bre_dic_values[i])):
            x2 = int(bre_dic_values[i][j]) - 1
            M_bon_2_f[x1, x2] = 0
    return bre_dic, M_bon_2_f


def modif_x(x, smiles, y):
    """
    加入新的原子后，更新 smiles
    :param x: 插入的位置
    :param smiles: 原来的 smiles
    :param y: 插入的单体
    :return: 新的smiles
    """
    x_lst = []  # 取出SMILES里原子的序号，'('用‘xx’代替
    for i in smiles:
        try:
            a = re.findall(r"\d+", i)[0]
            x_lst.append(int(a))
        except:
            x_lst.append('xx')
    x_index = x_lst.index(x)
    a = int(smiles[x_index][-2])
    if a == 0:
        smiles.insert(x_index + 1, y)
    else:
        smiles.insert(x_index + 1, '(,')
        smiles.insert(x_index + 2, y)
        smiles.insert(x_index + 3, '),')
    b = str(a + 1)
    smiles[x_index] = re.sub(r'!(.+?)!', f'!{b}!', smiles[x_index])
    return smiles


def produce_SMILES_num(new_MS, main_atom_index, new_adj):
    """
    生成用原子序号表示的 SMILES，
    :param new_MS: 新的步长矩阵
    :param main_atom_index: 主链原子序号
    :param new_adj: 新的连接关系
    :param M_atom_H: H原子序号
    :param yn: 判断是否显示 H
    :return: SMILES_num
    """
    x = []  # 对原子序号进行改装
    for i in range(np.shape(new_MS)[0]):
        if (i + 1) in main_atom_index:
            x.append(f'{i + 1},!1!')
        else:
            x.append(f'{i + 1},!0!')
    smiles = []  # 存改装的smiles
    smiles_f = []  # 记录加入过的原子序号
    for i in main_atom_index:  # 主链原子序号加入 smiles_f，经过改装的加入 smiles
        smiles.append(x[i - 1])
        smiles_f.append(i)
    L = np.shape(new_MS)[0]
    while (len(smiles_f) != L):
        for i in smiles_f:
            ss = new_adj[i - 1]
            ss = list(set(ss) - set(smiles_f))
            ss.sort(key=new_adj[i - 1].index)
            for j in ss:
                aa = x[j - 1]
                smiles = modif_x(x=i, smiles=smiles, y=aa)
                smiles_f.append(j)
    return smiles


def M_S_X(n, M_S):
    """
    取步长为 n 矩阵
    :param n: 步长数
    :param M_S: 步长矩阵
    :return: 步长为 n 的步长矩阵
    """
    Y = np.zeros(np.shape(M_S))
    s = np.where(M_S == n)
    Y[s[0], s[1]] = n
    Y = np.array(Y)
    return Y


def del_endpoint(M_S_A):
    """
    去除端点性原子
    :param M_S_A: 相邻矩阵
    :return: 度为 1 的行列化为 0后的相邻矩阵
    """
    n = np.shape(M_S_A)[0]
    du_lst = []  # 存度为 1 的原子编号
    M_S_A_d = copy.deepcopy(M_S_A)
    du_dic = {}
    for i in range(n):
        M_S_A_d[i, i] = np.sum(M_S_A[i, :])
        du_dic[i] = np.sum(M_S_A[i, :])
    # 找度为 1 的
    for i in range(n):  # 去掉
        if du_dic[i] == 1:
            du_lst.append(i)
    M_S_A[du_lst, :] = 0
    M_S_A[:, du_lst] = 0
    return du_lst, M_S_A  # du_lst:度为 1 的列表   M_S_A：度为 1 的行列化为 0后的矩阵


def floyd(M_S_A):
    """
    Floyd 算法
    :param M_S_A: 相邻矩阵
    :return: dis:步长矩阵      path: 路由矩阵
    """
    dis = copy.deepcopy(M_S_A)  # 邻接矩阵
    dis = np.where(dis == 0, inf, dis)  # 让0变为无穷，不然会默认0是最小
    n = np.shape(M_S_A)[0]  # 删掉端点原子后的原子数
    for i in range(n):
        dis[i, i] = 0  # 改对角线元素
    path = np.zeros((n, n), dtype=int)  # 初始化路由矩阵，让它都是零
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dis[i][k] + dis[k][j] < dis[i][j]:
                    dis[i][j] = dis[i][k] + dis[j][k]  # 找到经过k点时路径更短，接受这个更短的路径长度
                    path[i][j] = k  # 路由矩阵记录路径
    return dis, path  # dis:步长矩阵      path: 路由矩阵


def del_re(lst_x):
    """
    去重 以及保留连接关系
    :param lst_x: 需要处理的列表
    :return: 去重后的列表
    """
    lst_x_1 = copy.deepcopy(lst_x)
    for i in lst_x_1:
        i = i.sort()
    lst_x_0 = []
    for i in lst_x_1:
        if i not in lst_x_0:
            lst_x_0.append(i)
    lst_x_2 = []
    for i in lst_x_0:
        cyc_index = lst_x_1.index(i)
        lst_x_2.append(lst_x[cyc_index])
    lst_x = np.array(lst_x_2)
    return lst_x


def find_ben_modify_bon(M_bon_, cyc_six):
    """
    找苯环以及修改键值
    :param M_bon_: 键值矩阵
    :param cyc_six: 六元环
    :return: 苯环原子编号；苯环；M_bon_1:新的键值矩阵(1.5); M_bon_3:新的键值矩阵(4)
    """
    M_bon_1 = copy.deepcopy(M_bon_)
    M_bon_2 = copy.deepcopy(M_bon_)
    M_bon_3 = copy.deepcopy(M_bon_)
    cyc_6_list = cyc_six.tolist()
    ben_num = []
    cyc_ben = []
    for i in cyc_6_list:
        link_1 = M_bon_2[i[0] - 1, i[1] - 1]  # 减 1 是从 0 开始
        link_2 = M_bon_2[i[1] - 1, i[2] - 1]
        link_3 = M_bon_2[i[2] - 1, i[3] - 1]
        link_4 = M_bon_2[i[3] - 1, i[4] - 1]
        link_5 = M_bon_2[i[4] - 1, i[5] - 1]
        link_6 = M_bon_2[i[5] - 1, i[0] - 1]
        link_0 = [link_1, link_2, link_3, link_4, link_5, link_6]
        link_sum = sum(link_0)
        if link_sum > 8:
            for j in range(6):
                if i[j] not in ben_num:
                    ben_num.append(i[j])
                k = j + 1
                if k == 6:
                    M_bon_1[i[j] - 1, i[0] - 1] = 1.5
                    M_bon_1[i[0] - 1, i[j] - 1] = 1.5
                    M_bon_3[i[j] - 1, i[0] - 1] = 4
                    M_bon_3[i[0] - 1, i[j] - 1] = 4
                else:
                    M_bon_1[i[j] - 1, i[k] - 1] = 1.5
                    M_bon_1[i[k] - 1, i[j] - 1] = 1.5
                    M_bon_3[i[j] - 1, i[k] - 1] = 4
                    M_bon_3[i[k] - 1, i[j] - 1] = 4
    for i in cyc_6_list:
        xx = list(set(i) & (set(ben_num)))
        if len(xx) == 6:
            cyc_ben.append(i)
    cyc_ben = np.array(cyc_ben)
    return ben_num, cyc_ben, M_bon_1, M_bon_3


def M_del(M, del_n):
    """
    删除列表行列后新的矩阵
    :param M: 需要处理的矩阵
    :param del_n: 需要删除的行列
    :return: 新的矩阵
    """
    M_f = np.array(M)
    M_f = np.delete(M_f, del_n, 0)  # 0 是行
    M_f = np.delete(M_f, del_n, 1)  # 1 是列
    return M_f


def cyc_6(M_S_A, M_S):
    """
    找六元环
    :param M_S_A: 相邻矩阵
    :param M_S: 步长矩阵
    :return:
    """
    n = np.shape(M_S_A)[0]
    # 删除端点原子
    M_S_A_1 = copy.deepcopy(M_S_A)  # 这里需要用copy拷贝
    du_lst, M_S_A_1 = del_endpoint(M_S_A=M_S_A_1)
    del_num = copy.deepcopy(du_lst)
    while du_lst:
        du_lst, M_S_A_1 = del_endpoint(M_S_A=M_S_A_1)
        del_num += du_lst
    # 去除端点性原子后的原子序号对应表
    m_dict = {}
    j = 0
    for i in range(n):
        if i not in del_num:
            m_dict[j] = i + 1
            j += 1
    # 去除端点性原子后 新相邻矩阵和步长矩阵
    M_S_A_2 = copy.deepcopy(M_S_A)
    M_S_A_2 = M_del(M=M_S_A_2, del_n=del_num)
    M_S_2 = M_del(M=M_S, del_n=del_num)
    dis, path = floyd(M_S_A=M_S_A_2)
    n = np.shape(M_S_A_2)[0]  # 删掉端点原子后的原子数
    M_S_B = M_S_X(n=2, M_S=dis)
    cyc_six = []
    for i in range(n):
        ssw = np.where(M_S_B[:, i] == 2)[0]  # 取 M 里步长为 2 的点
        combin = list(itertools.combinations(ssw, 2))
        for j in combin:
            k = path[j[0]][j[1]]
            if int(M_S_2[i, k]) == 3 and int(M_S_2[j[0], j[1]]) == 2:
                m = path[j[0]][i]
                n = path[j[1]][i]
                if m != n:
                    cyc_six.append([m_dict[i], m_dict[m], m_dict[j[0]], m_dict[k], m_dict[j[1]], m_dict[n]])
    cyc_six = del_re(cyc_six)
    return cyc_six


def find_main(new_MS, new_adj, ss_w):
    """
    找主链
    :param new_MS: 新的步长矩阵
    :param new_adj: 新的连接关系
    :param ss_w: 最大步长对应的位置
    :param M_atom_H: H原子序号列表
    :return: 主链原子序号
    """
    start_atom = int(ss_w[0][0])
    end_atom = int(ss_w[1][0])
    body_atom = start_atom
    index_atom = []  # 存实际原子号
    index_atom.append(start_atom + 1)
    for i in range(np.shape(new_MS)[0]):
        ss = new_adj[body_atom]
        ss = list(set(ss) - set(index_atom))
        if len(ss) != 0:
            for j in ss:
                if int(new_MS[j - 1, start_atom]) + int(new_MS[j - 1, end_atom]) == int(new_MS[start_atom, end_atom]):
                    body_atom = j - 1
                    index_atom.append(j)
    return index_atom


def add_element(smiles_lst, M_atom_nH, ben_num, sym):
    """
    加元素
    :param smiles_lst: 原子编号 SMILES
    :param M_atom: 原子信息
    :param ben_num: 苯环原子编号
    :return: 正则处理过的原子编号 SMILES；元素表示的 SMILES
    """
    M_atom_nH_f = copy.deepcopy(M_atom_nH)
    X = ['B', 'C', 'N', 'O', 'S', 'P', 'F', 'Cl', 'Br', 'I', 'b', 'c', 'n', 'o', 's', 'p']
    if sym == 0:
        smiles = ''.join(smiles_lst)
        smiles = re.sub(r'!(.+?)!', '', smiles)  # 正则匹配
        smiles_lst = smiles.split(',')
    smiles_atom_lst = []
    for i in range(len(M_atom_nH_f)):
        if (i + 1) in ben_num:
            M_atom_nH_f[i] = M_atom_nH_f[i].lower()  # 更改苯环原子
        if M_atom_nH_f[i] not in X:
            M_atom_nH_f[i] = f'[{M_atom_nH_f[i]}]'  # 更改非X类型的
    for i in range(len(smiles_lst)):
        if smiles_lst[i].isdigit() == True:
            x = M_atom_nH_f[int(smiles_lst[i]) - 1]
            smiles_atom_lst.append(x)
        else:
            smiles_atom_lst.append(smiles_lst[i])
    return smiles_lst, smiles_atom_lst


def add_bond(M_adj, smiles_lst, smiles_atom_lst, M_atom, M_bon_modif):
    """
    SMILES 加键
    :param M_adj: 连接关系
    :param M_atom_H: 氢原子编号
    :param smiles_lst: 序号表示的 SMILES
    :param smiles_atom_lst: 元素符号表示的 SMILES
    :param M_atom: 原子信息
    :param M_bon_modif: 新的键值关系
    :return: 加完键的序号表示的 SMILES；加完键的元素符号表示的 SMILES
    """
    X = ['b', 'c', 'n', 'o', 's', 'p']
    biaoji = []
    for i in range(len(M_adj) - 1):
        x1 = i + 1
        x2_lst = M_adj[i]
        for x2 in x2_lst:
            if x2 not in biaoji:
                x11 = str(x1)
                x22 = str(x2)
                bond_x = M_bon_modif[x1 - 1, x2 - 1]
                if (M_atom[x1 - 1] in X) and (M_atom[x2 - 1] in X) and (bond_x == 1):
                    x1_index = smiles_lst.index(x11)
                    x2_index = smiles_lst.index(x22)
                    x_index = max(x1_index, x2_index)
                    smiles_lst.insert(x_index, '-')
                    smiles_atom_lst.insert(x_index, '-')
                    biaoji.append(x1)
                elif bond_x == 2:
                    x1_index = smiles_lst.index(x11)
                    x2_index = smiles_lst.index(x22)
                    x_index = max(x1_index, x2_index)
                    smiles_lst.insert(x_index, '=')
                    smiles_atom_lst.insert(x_index, '=')
                    biaoji.append(x1)
                elif bond_x == 3:
                    x1_index = smiles_lst.index(x11)
                    x2_index = smiles_lst.index(x22)
                    x_index = max(x1_index, x2_index)
                    smiles_lst.insert(x_index, '#')
                    smiles_atom_lst.insert(x_index, '#')
                    biaoji.append(x1)
    return smiles_lst, smiles_atom_lst


def add_bre(bre_dic, smiles_lst, smiles_atom_lst):
    """
    SMILES 加断裂关系
    :param bre_dic: 断键字典
    :param smiles_lst: 加过连接关系的字典
    :param smiles_atom_lst: 加过连接关系的字典
    :return:
    """
    bre_dic_f = copy.deepcopy(bre_dic)
    bre_dic_keys = list(bre_dic_f.keys())
    bre_dic_keys.sort(key=smiles_lst.index)
    for i in range(len(bre_dic_keys)):
        bre_dic_f[bre_dic_keys[i]].sort(key=smiles_lst.index)
    bre_dic_keys_f = copy.deepcopy(bre_dic_keys)
    x = [f',!{i + 1}!' for i in range(3 * len(bre_dic_keys))]
    x_f = copy.deepcopy(x)
    for i in range(len(bre_dic_keys)):
        digit_n = re.findall("\d+", bre_dic_keys[i])
        digit_x = digit_n[1:]
        bre_dic_values_x = bre_dic_f[bre_dic_keys_f[i]]
        # 先插值
        if len(bre_dic_values_x) != 0:
            for j in range(len(bre_dic_values_x)):
                bre_dic_keys[i] = bre_dic_keys[i] + x[0]
                k_index = bre_dic_keys_f.index(bre_dic_values_x[j])
                bre_dic_keys[k_index] = bre_dic_keys[k_index] + x[0]
                x.pop(0)
                bre_dic_f[bre_dic_values_x[j]].remove(digit_n[0])
            if len(digit_x) != 0:
                for k in range(len(digit_x) - 1, -1, -1):
                    x.insert(0, f',!{digit_x[k]}!')
                    x.sort(key=x_f.index)
        else:
            if len(digit_x) != 0:
                for k in range(len(digit_x) - 1, -1, -1):
                    x.insert(0, f',!{digit_x[k]}!')
                    x.sort(key=x_f.index)
    for i in range(len(bre_dic_keys_f)):
        digit_n = re.findall("\d+", bre_dic_keys[i])
        digit_x = digit_n[1:]
        x_index = smiles_lst.index(bre_dic_keys_f[i])
        for j in range(len(digit_x)):
            if int(digit_x[j]) < 10:
                smiles_lst.insert(x_index + j + 1, f',!{digit_x[j]}!')
                smiles_atom_lst.insert(x_index + j + 1, f'{digit_x[j]}')
            else:
                smiles_lst.insert(x_index + j + 1, f',!%{digit_x[j]}!')
                smiles_atom_lst.insert(x_index + j + 1, f'%{digit_x[j]}')
    return smiles_lst, smiles_atom_lst


def M_del_H(M, index_x):
    """
    矩阵去氢
    :param M: 需要处理的矩阵
    :param index_x: 非氢索引
    :return: 去氢后的矩阵
    """
    M_f = copy.deepcopy(M)
    M_f = M_f[index_x, :]
    M_f = M_f[:, index_x]
    return M_f


def sort_1(a):
    """
    对array排序，返回对应位置的大小
    :param a: 需要处理的array
    :return: 对应位置的大小
    """
    lst_array = copy.deepcopy(a)
    lst_array_f = copy.deepcopy(a)
    lst_1 = sorted(lst_array)
    lst_1_de = list(set(lst_1))
    lst_1_de.sort(key=lst_1.index)
    for i in range(0, len(lst_1_de)):
        ss = np.where(lst_array == lst_1_de[i])
        lst_array_f[ss] = i + 1
    return lst_array_f


def sort_2(a, prime_table):
    """
    对array排序，返回对应位置的大小的素数
    :param a: 需要处理的array
    :return: 对应位置的大小的素数
    """
    lst_array = copy.deepcopy(a)
    lst_array_f = copy.deepcopy(a)
    lst_1 = sorted(lst_array)
    lst_1_de = list(set(lst_1))
    lst_1_de.sort(key=lst_1.index)
    for i in range(0, len(lst_1_de)):
        ss = np.where(lst_array == lst_1_de[i])
        lst_array_f[ss] = prime_table[i]
    return lst_array_f


def sort_3(a1, a2):
    """
    根据两个rank排序，a1优先，a1相同看a2
    :param a1: rank0
    :param a2: rank_mult
    :return: 新的 rank
    """
    a1_f = copy.deepcopy(a1)
    a2_f = copy.deepcopy(a2)
    a_f = copy.deepcopy(a1)
    a1_f_s = sorted(a1_f)
    lst_1_de = list(set(a1_f))
    lst_1_de.sort(key=a1_f_s.index)
    j = 1
    for i in range(0, len(lst_1_de)):
        ss = np.where(a1_f == lst_1_de[i])
        L = int(np.shape(ss)[1])
        if L == 1:
            a_f[ss] = j
            j += 1
        else:
            ss_2 = a2_f[ss]
            a3_s = sorted(ss_2)
            a3_de = list(set(a3_s))
            a3_de.sort(key=a3_s.index)
            for k in range(0, len(a3_de)):
                ss_3 = np.where(a2_f == a3_de[k])
                ss_3 = list(set(list(ss_3[0])) & set(list(ss[0])))
                a_f[ss_3] = j
                j += 1
    return a_f


def primes(n):
    """
    素数生成器
    :param n: n 以内
    :return: n 以内的素数
    """
    P = []
    f = []
    for i in range(n + 1):
        if i > 2 and i % 2 == 0:
            f.append(1)
        else:
            f.append(0)
    i = 3
    while i * i <= n:
        if f[i] == 0:
            j = i * i
            while j <= n:
                f[j] = 1
                j += i + i
        i += 2
    P.append(2)
    for x in range(3, n + 1, 2):
        if f[x] == 0:
            P.append(x)
    return P


def sym1(graph, x_atom):
    result = []
    new_graph = {}
    graph_keys = list(graph.keys())
    for i in range(len(graph_keys)):
        new_graph[graph_keys[i]] = []
    body = x_atom[0]
    for i in range(len(graph)):
        result.append(body)
        x1 = graph[body]
        ss = list(set(x1) - set(result))
        ss.sort(key=x1.index)
        try:
            body = ss[0]
        except:
            break
    for i in range(1, len(result)):
        new_graph[result[i - 1]].append(result[i])
        new_graph[result[i]].append(result[i - 1])
    smiles_lst = [str(i) for i in result]
    return smiles_lst, new_graph


def sort_rank_graph(x_atom=None, no_circle_graph=None):
    """
    # todo 需要重新生成连接关系的rank
    :param x_atom: rank序列
    :param no_circle_graph: 无环图
    :return: 排好序列的无环图
    """
    no_circle_graph_copy = copy.deepcopy(no_circle_graph)
    x_atom = [str(i) for i in x_atom]
    for i in no_circle_graph_copy:
        item = no_circle_graph_copy[i]
        item.sort(key=x_atom.index)
        no_circle_graph_copy[i] = item
    return no_circle_graph_copy


def gifToSMILES(gjf_path):
    MSI_gjf = msi_gjf(gjf_path=gjf_path)
    M_S_A = np.array(MSI_gjf['M_S_A'])
    M_S = np.array(MSI_gjf['M_S'])
    M_bon_ = np.array(MSI_gjf['M_bon_'])
    M_atom = MSI_gjf['M_atom']
    M_adj_H = MSI_gjf['M_adj_H']
    M_adj_nH_f = MSI_gjf['M_adj_nH']
    # 去氢
    index_nH = []
    M_adj_nH = []
    M_atom_nH = []
    atom_num = []
    connect_H_num = []
    for i in range(len(M_atom)):
        if M_atom[i] != 'H':
            index_nH.append(i)
            M_adj_nH.append(M_adj_nH_f[i])
            M_atom_nH.append(M_atom[i])
            atom_num.append(elements_table[M_atom[i]])
            connect_H_num.append(len(M_adj_H[i]))
    for i in range(len(M_adj_nH)):
        for j in range(len(M_adj_nH[i])):
            M_adj_nH[i][j] = index_nH.index(int(M_adj_nH[i][j]) - 1) + 1
    M_S_A_nH = M_del_H(M=M_S_A, index_x=index_nH)
    M_bon_nH = M_del_H(M=M_bon_, index_x=index_nH)
    M_S_nH = M_del_H(M=M_S, index_x=index_nH)
    n_atom_nH = len(index_nH)
    cyc_six = cyc_6(M_S_A=M_S_A_nH, M_S=M_S_nH)  # 找苯环 改键的类型
    ben_num, cyc_ben, M_bon_nH_1, M_bon_nH_2 = find_ben_modify_bon(M_bon_=M_bon_nH, cyc_six=cyc_six)
    # x_atom 优先级顺序 小的在后面
    graph, x_atom, rank_0, sym = get_graph(n_atom_nH=n_atom_nH, atom_num=atom_num, connect_H_num=connect_H_num,
                                           M_S_A_nH=M_S_A_nH, M_bon_2_nH=M_bon_nH_2, M_S_nH=M_S_nH, M_adj_nH=M_adj_nH)
    if sym == 1:
        smiles_lst, new_graph = sym1(graph=graph, x_atom=x_atom)
        bre_dic, M_bon_2_new = break_bond(graph=graph, new_graph=new_graph, M_bon_2=M_bon_nH_2)
    else:
        graph = exchange_graph(graph=graph)
        result, no_circle_graph, unique_link_graph = code_king_DFS(graph=graph, start=str(x_atom[-1]))
        bre_dic = get_break_graph(graph=graph, new_graph=no_circle_graph)
        print('断掉的连接关系:bradk_graph：', bre_dic)
        # no_circle_graph 需要重新排优先级
        # result, sec_no_circle_graph, unique_link_graph = code_king_DFS(graph=no_circle_graph, start=str(x_atom[-1]))
        sort_rank_graph(x_atom=x_atom, no_circle_graph=no_circle_graph)
        # 只需要找到度为0的就行
        zero_list = get_degree_zero(no_circle_graph=no_circle_graph)
        # max_road, final_result, mainList, sideList = get_max_road(atom_list=zero_list, no_circle_graph=no_circle_graph,start=str(x_atom[-1]))
        max_final_result, max_main_list, max_side_list = get_max_road(atom_list=zero_list, no_circle_graph=no_circle_graph,start=str(x_atom[-1]))
        print(f'\n***max_road,长度为{len(max_main_list)}，如下：{max_main_list}')
        print(f'\n***unique_link_graph:{unique_link_graph}')
        side_set_list = find_side(graph=no_circle_graph, result=max_final_result)
        print('侧链集合：', side_set_list)
        final_side = get_final_side(side_set_list=side_set_list)
        print('升序侧链集合：', final_side)
        smiles_list = gjf_to_smiles(unique_link_graph=unique_link_graph, main_list=max_main_list, final_side=final_side)
        print('SMILES:smiles_list：', smiles_list)
        smiles_lst = ','.join(smiles_list)
        print('SMILES:smiles结果：', smiles_lst)
        bre_dic = get_break_graph(graph=graph, new_graph=no_circle_graph)
        print('断掉的连接关系:bradk_graph：', bre_dic)
    smiles_lst, smiles_atom_lst = add_element(smiles_lst=smiles_lst, M_atom_nH=M_atom_nH, ben_num=ben_num, sym=sym)
    smiles_lst, smiles_atom_lst = add_bond(M_adj=M_adj_nH, smiles_lst=smiles_lst,
                                           smiles_atom_lst=smiles_atom_lst, M_atom=M_atom_nH, M_bon_modif=M_bon_nH_1)
    smiles_lst, smiles_atom_lst = add_bre(bre_dic=bre_dic, smiles_lst=smiles_lst, smiles_atom_lst=smiles_atom_lst)
    SMILES = ''.join(smiles_atom_lst)
    return SMILES


if __name__ == "__main__":
    t1 = time.time()
    gjf_path = '../test/111.gjf'
    SMILES = gifToSMILES(gjf_path=gjf_path)
    t2 = time.time()
    print(SMILES)
    print(t2 - t1)
