# coding: utf-8
# @FileName: oj_1.py
# @Time: 2022/8/14 14:39
# @Author: QHB

"""
=================================================================
输入描述: 把这一行用空格分开的数字变为列表
==================================================================
"""

import sys

d = []
while True:
    try:
        dd = list(map(int, sys.stdin.readline().strip().split()))
        if not dd:
            break
        d.append(dd)
    except:
        break
print(d)
