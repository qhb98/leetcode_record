# coding: utf-8
# @FileName: oj_1.py
# @Time: 2022/8/14 14:39
# @Author: QHB

"""
=================================================================
输入描述: 输入第一行有三个整数N M K, 接下来N行, 每行M个整数为输入的矩阵
==================================================================
"""

import sys
# 读取第一行, 分割
list_num = sys.stdin.readline().split()
N, M, K = [int(list_num[i]) for i in range(len(list_num))]
for i in range(N):
    # 依次遍历所有行, 每行存入变量line进行处理
    line = sys.stdin.readline()