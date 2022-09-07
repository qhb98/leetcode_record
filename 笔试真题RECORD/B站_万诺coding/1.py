# coding: utf-8
# @FileName: 1.py
# @Time: 2022/9/1 13:43
# @Author: QHB

"""

这是一个b站的up主, 主要是可以看到一些笔试的真题(比较难的那种题, easy题就不需要了)的正确解法和思路讲解, 专门用于针对笔试的能力范围做 查漏补缺

"""
"""
2020阿里秋招笔试真题:
将烧饼摆在一排的n个盘子上, 其中第i个盘子中有S_i个烧饼, 但是对于一次吃烧饼操作, 参赛者每次选择1到n的某个整数x, 
将1, 2,..., x-1, x盘子中的烧饼都吃掉一个. 如果1到x的某个盘子里没有烧饼了, 那么这个x不能被选. 
假设胃容量无限大, 最多可以吃掉多少个烧饼?

输入: 
    第一行一个整数n表示盘子的个数
    第二行n个整数S_i表示盘子i里最初的烧饼个数
    

# 核心: 每个盘子中最多吃多少个烧饼取决于在这个盘子前最少的那个数量
# dp[i] = min(dp[i - 1], nums[i])

"""

def eat_shaobin(n, nums):
    eat_min = nums[0]
    sum = nums[0]
    for num in nums:
        eat_min = min(eat_min, num)
        sum += eat_min
    return sum






