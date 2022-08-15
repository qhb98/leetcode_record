# coding: utf-8
# @FileName: test_62.py
# @Time: 2022/8/15 21:30
# @Author: QHB

# 第 62 题  不同路径

def differ_routes(m, n):
    dp_table = [[1] * n for _ in range(m)]
    # 初始化
    for i in range(m):
        dp_table[i][0] = 1
    for j in range(n):
        dp_table[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp_table[i][j] = dp_table[i - 1][j] + dp_table[i][j - 1]
    return dp_table[m - 1][n - 1]


print(differ_routes(5, 5))
