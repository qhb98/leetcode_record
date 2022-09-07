# coding: utf-8
# @FileName: 3.py
# @Time: 2022/9/1 14:32
# @Author: QHB

"""
华为 20220831 笔试真题

输入一个n*m的迷宫, 迷宫中0为路, 1为墙, 2为起点, 3为终点, 4为陷阱, 6为炸弹. 士兵只能向 上下左右 四个方向移动.
如果路径上为墙, 不能移动. 已知每走一步需要花费1个单位的时间, 走到陷阱上需要花费3个单位时间, 走到炸弹上将会激活炸弹将炸弹上下左右的墙炸为路.
注意点:
    1. 炸弹只能毁墙, 不会炸掉陷阱
    2. 炸弹、陷阱只能发挥一次左右
    3. 迷宫最大为 25*25
    4. 用例保证士兵一定有方法能到终点

输入:
    第一行 n m
    第二行 n*m的矩阵


"""
from collections import deque

n, m = map(int, input().split(" "))
matrix = []
for i in range(n):
    matrix.append([int(c) for c in input().split(" ")])
    for j in range(len(matrix[i])):
        if matrix[i][j] == 2:
            # 记录起点
            st = (i, j)
        elif matrix[i][j] == 3:
            # 记录终点
            ed = (i, j)

def bfs():
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    queue = deque()




















