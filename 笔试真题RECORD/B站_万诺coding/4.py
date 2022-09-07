# coding: utf-8
# @FileName: 4.py
# @Time: 2022/9/3 15:00
# @Author: QHB

"""
滑动窗口解题模版

题目应用场景:
    关键词: 满足...条件(计算结果, 出现次数, 同时包含)
    最长/最短
    子串/子数组/子序列

使用思路 -- 寻找最长:
    核心: 左右双指针(L, R)在起始点, R向右逐位滑动循环
    每次滑动过程中, 如果窗内元素满足条件, R向右扩大窗口, 并且更新最优结果
    如果窗内元素不满足条件, L向右缩小窗口
    R到达结尾

使用思路 -- 寻找最短:
    核心: 左右双指针(L, R)在起始点, R向右逐位滑动循环
    每次滑动过程中, 如果窗内元素满足条件, L向右缩小窗口, 并且更新最优结果
    如果窗内元素不满足条件, R向右扩大窗口
    R到达结尾

https://www.bilibili.com/video/BV1V44y1s7zJ/?spm_id_from=333.788.recommend_more_video.-1&vd_source=7111d4cfa9354342c253c06ecdd64e2f

"""

"""
# 最长的模板
初始化 left, right, result, best_result
while 右指针没有到结尾:
    窗口扩大, 加入right对应元素, 更新当前result
    while result不满足要求:
        窗口缩小, 移除left对应元素, left右移
    更新最优结果best_result
    right ++ 
return best_result
"""

# 209 长度最小的子数组
