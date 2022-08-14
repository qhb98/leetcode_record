# coding: utf-8
# @FileName: test_349.py
# @Time: 2022/8/14 20:08
# @Author: QHB


"""
第 349 题  给定两个数组, 编写一个函数来计算它们的交集

一种哈希数据结构: unordered_set

"""


def intersection(nums1, nums2):
    # 两个数组先变成集合，求交集后还原为数组
    return list(set(nums1) & set(nums2))


