# coding: utf-8
# @FileName: bubble_sort.py
# @Time: 2022/8/16 13:50
# @Author: QHB

# 冒泡排序  O(n^2)


def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort(arr=[5, 4, 3, 2, 1]))
