# coding: utf-8
# @FileName: test_70.py
# @Time: 2022/8/15 11:19
# @Author: QHB

# 爬楼梯

def climb_stairs(n):
    # dp_table
    dp_table = [0] * n
    # 初始化
    dp_table[0] = 1
    dp_table[1] = 2
    # 递推公式
    for i in range(2, n):
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2]
    return dp_table[-1]


print(climb_stairs(5))
