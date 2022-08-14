# coding: utf-8
# @FileName: test_344.py
# @Time: 2022/8/14 21:17
# @Author: QHB

"""

第 344 题 反转字符串


"""


def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
