# coding: utf-8
# @FileName: bfs.py
# @Time: 2022/8/13 11:45
# @Author: QHB

# 注意对比 BFS

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


# BFS算法
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
