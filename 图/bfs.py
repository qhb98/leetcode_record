# coding: utf-8
# @FileName: bfs.py
# @Time: 2022/8/16 18:06
# @Author: QHB

# 图的广度优先搜索


# 使用函数deque创建一个双端队列
from collections import deque

# 使用字典创建图
graph = {"A": ["B", "D", "F"], "B": ["C", "E"], "D": ["C"], "F": ["G", "H"], "C": [], "E": [], "G": [], "H": []}


def search(start_node):
    search_queue = deque()
    search_queue += graph[start_node]
    # 这个数组用于记录检查过的节点
    searched = []

    # 只要节点列表不为空
    while search_queue:
        # 取出节点列表中最左边的节点
        node = search_queue.popleft()
        print(node, end=' ')
        # 如果这个节点没检查过
        if node not in searched:
            # 检查这个节点是否为终点"G"
            if node == 'G':
                print("\nfind the destination!")
                return True
            else:
                # 将此节点的相邻节点都添加到节点列表中
                search_queue += graph[node]
                # 将这个节点标记为检查过
                searched.append(node)

    # 如果节点列表为空仍没找到终点，则返回False
    return False


print(search("A"))
