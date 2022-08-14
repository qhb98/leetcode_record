# coding: utf-8
# @FileName: oj_1.py
# @Time: 2022/8/14 14:39
# @Author: QHB

"""
=================================================================
输入描述: 输入数据有多组, 每行表示一组输入数据.
        每行的第一个整数为整数的个数n.
        接下来n个正整数, 即需要求和的每个正整数.
输入例子:
    4 1 2 3 4
    5 1 2 3 4 5
==================================================================
输出描述: 每组数据输出求和的结果
输出例子:
    10
    15
==================================================================
"""

while True:
    try:
        num = list(map(int, input().split(" ")))
        # ACM模式里必须要用print将最终结果打印到控制台, 而不是return
        print(sum(num[1:]))
    except:
        break
