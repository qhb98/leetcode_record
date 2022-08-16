# coding: utf-8
# @FileName: shell_sort.py
# @Time: 2022/8/16 14:04
# @Author: QHB

# 希尔排序 O(n log n)

def shell_sort(arr):
    import math
    gap = 1
    while gap < len(arr) / 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = math.floor(gap / 3)
    return arr
