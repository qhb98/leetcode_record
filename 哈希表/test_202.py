# coding: utf-8
# @FileName: test_202.py
# @Time: 2022/8/14 21:04
# @Author: QHB

"""
第 202 题 快乐数

使用哈希法，来判断这个sum是否重复出现

"""


def calculate_happy(num):
    sum_ = 0
    while num:
        sum_ += (num % 10) ** 2
        num = num // 10
    return sum_


def is_happy(n):
    record = set()
    while True:
        # 计算平方和
        n = calculate_happy(n)
        if n == 1:
            return True
        if n in record:
            return False
        else:
            record.add(n)
