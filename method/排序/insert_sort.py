# coding: utf-8
# @FileName: insert_sort.py
# @Time: 2022/8/16 14:00
# @Author: QHB


# 插入排序 O(n^2)


def insertion_sort(arr):
    for i in range(len(arr)):
        pre_index = i - 1
        current = arr[i]
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current
    return arr


print(insertion_sort(arr=[5, 4, 3, 2, 1]))
