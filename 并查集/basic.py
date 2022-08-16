# coding: utf-8
# @FileName: basic.py
# @Time: 2022/8/16 15:44
# @Author: QHB

"""
并查集 union-find sets 是一种精巧的数据结构, 主要用于处理一些不相交集合的合并问题, 又称为 不相交集.
主要用于 求连通子图、求最小生成树的Kruskal算法 和 求最近公共祖先的LCA 等

并查集的基本操作: 初始化init  查询find  合并 union

参考链接: http://www.srcmini.com/1627.html

"""


# 初始化
def init_fa(n):
    fa = [0] * n
    global fa
    for i in range(n):
        fa[i] = i


def find(i):
    # 递归出口, 当到达了祖先位置, 就返回祖先
    if fa[i] == i:
        return i
    else:
        # 不断向上查找祖先
        return find(fa[i])


def union(i, j):
    # 找到i的祖先
    i_fa = find(i)
    # 找到j的祖先
    j_fa = find(j)
    # i的祖先指向j的祖先
    fa[i_fa] = j_fa
