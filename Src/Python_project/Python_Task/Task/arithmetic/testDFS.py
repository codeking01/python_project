# auth: code_king
# time: 2022/10/18 19:40
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
graph = {
    'A': ['B', 'D', 'C'],
    'B': ['A', 'E','P'],
    'C': ['A', 'F'],
    'D': ['A', 'G'],
    'E': ['B', 'I', 'M'],
    'F': ['C', 'H'],
    'G': ['D', 'I','L'],
    'H': ['F', 'I'],
    'I': ['H', 'J', 'G', 'E'],
    'J': ['I'],
    'M': ['E','N'],
    'N': ['M'],
    'P': ['B'],
    'L': ['G'],
}


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
    result = DFS(graph, 'A')
    print(result)
    print('***********')
    final_result = find_main(graph, result, 'J')
    print(final_result)
