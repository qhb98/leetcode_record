# coding: utf-8
# @FileName: heap_sort.py
# @Time: 2022/8/16 15:14
# @Author: QHB

# 堆排序  heapsort

def build_max_heap(arr):
    import math
    for i in range(math.floor(len(arr) / 2), -1, -1):
        heapify(arr, i)


def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < arr_len and arr[left] > arr[largest]:
        largest = left
    if right < arr_len and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heap_sort(arr):
    global arr_len
    arr_len = len(arr)
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        arr_len -= 1
        heapify(arr, 0)
    return arr
