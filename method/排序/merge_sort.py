# coding: utf-8
# @FileName: merge_sort.py
# @Time: 2022/8/16 14:06
# @Author: QHB

# 归并排序  O(n log n)  分治法的思想
"""
步骤1 申请空间, 使其大小为两个已经排序序列之和, 该空间用来存放合并后的序列
步骤2 设定两个指针, 最初位置分别为两个已经排序序列的起始位置
步骤3 比较两个指针所指向的元素, 选择相对小的元素放入到合并空间中, 并移动指针到下一位置
步骤4 重复步骤3 直到某一指针达到序列尾
步骤5 将另一序列剩下的所有元素直接复制到合并序列尾

"""


def merge_sort(arr):
    import math
    if len(arr) < 2:
        return arr
    middle = math.floor(len(arr) / 2)
    left, right = arr[0:middle], arr[middle:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 这个时候left或者right中必然已经有一个是空的, 再把非空的, 即大的那个append进去
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


print(merge_sort(arr=[5, 4, 3, 2, 1]))
