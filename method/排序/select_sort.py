# coding: utf-8
# @FileName: select_sort.py
# @Time: 2022/8/16 13:55
# @Author: QHB

# 选择排序 O(n^2)


def select_sort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # i 不是最小数的索引时，将 i 和最小数的索引进行交换
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


print(select_sort(arr=[5, 4, 3, 2, 1]))
