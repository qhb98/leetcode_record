# coding: utf-8
# @FileName: test_785.py
# @Time: 2022/8/16 17:00
# @Author: QHB

# LC第 785 题  判断二分图

def is_bipartite(graph):
    n = len(graph)
    vis = [-1 for i in range(n)]

    def dfs(p, u):
        for v in graph[u]:
            if v == p:
                continue
            elif vis[v] == -1:
                vis[v] = vis[u] ^ 1
                if not dfs(u, v):
                    return False
            elif vis[v] != -1 and vis[v] ^ vis[u] == 0:
                return False
        return True

    for i in range(n):
        if vis[i] == -1:
            vis[i] = 0
            if not dfs(-1, i):
                return False
    return True


print(is_bipartite(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
