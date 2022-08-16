# coding: utf-8
# @FileName: quick_sort.py
# @Time: 2022/8/16 14:33
# @Author: QHB

# 快速排序
"""
快速排序的最坏运行情况是 O(n²)，比如说顺序数列的快排
但它的平摊期望时间是 O(nlogn)，且 O(nlogn) 记号中隐含的常数因子很小，
比复杂度稳定等于 O(nlogn) 的归并排序要小很多
所以，对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序

步骤1 从数列中挑出一个元素, 称为 基准pivot
步骤2 分区  重新排序数列, 所有元素比基准值小的摆放在基准前面, 所有元素比基准值大的摆在基准的后面
步骤3 递归地把小于基准值元素的子数列和大于基准值元素的子数列排序


参考链接: http://data.biancheng.net/view/117.html

"""


def quick_sort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partition_index = partition(arr, left, right)
        quick_sort(arr, left, partition_index - 1)
        quick_sort(arr, partition_index + 1, right)
    return arr


def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)
    return index - 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


print(quick_sort(arr=[5, 4, 3, 2, 1]))
