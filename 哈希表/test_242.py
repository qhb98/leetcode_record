# coding: utf-8
# @FileName: test_242.py
# @Time: 2022/8/14 19:56
# @Author: QHB


"""
力扣第 242 题, 有效的字母异位词


"""


def is_anagram(s, t):
    """

    :param s: 给定初始字符串
    :param t: 给定初始字符串
    :return: 返回判断结果
    """
    record = [0] * 26
    for i in range(len(s)):
        # 并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
        record[ord(s[i]) - ord("a")] += 1
    for i in range(len(t)):
        record[ord(t[i]) - ord("a")] -= 1
    for i in range(26):
        if record[i] != 0:
            # record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
            return False
    return True