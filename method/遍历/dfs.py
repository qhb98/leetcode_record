# coding: utf-8
# @FileName: bfs.py
# @Time: 2022/8/13 11:45
# @Author: QHB

"""

DFS depth-first-search 是搜索算法的一种, 是沿着树的深度遍历树的节点, 尽可能深地搜索树的分支.
当节点v的所有边都已被探寻过, 搜索将回溯到发现节点v的那条边的起始节点, 这个过程一直进行到已发现从
源节点可达的所有节点为止. 如果还存在未被发现的节点, 则选择其中一个作为源节点并重复以上过程, 整个
进程反复进行直到所有节点都被访问为止.

DFS广义来讲, 只要最新产生的结点先进行扩展就是DFS.
有全部保留和不全部保留产生的结点两种情况.

"""
# 注意对比 BFS

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


# DFS算法
def bfs(graph1, star):
    queue = []  # 定义一个队列
    seen = set()  # 建立一个集合，集合就是用来判断该元素是不是已经出现过
    queue.append(star)  # 将起点放入
    seen.add(star)  # 同上
    while len(queue) > 0:  # 当队列里还有东西时
        ver = queue.pop(-1)  # 取出队尾元素
        notes = graph1[ver]  # 查看graph里面的key,对应的邻接点
        for i in notes:  # 遍历邻接点
            if i not in seen:  # 如果该邻接点还没出现过
                queue.append(i)  # 存入queue
                seen.add(i)  # 存入集合
        print(ver)  # 打印队头元素


print(bfs(graph, "A"))
