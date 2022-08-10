# coding: utf-8
# @FileName: :binary_search.py
# @Time: 2022/8/10 16:33
# @Author: QHB

"""
二分法 主要考虑边界条件的定义要正确, 对于区间的定义要遵循 保持不变量规则

两种写法:

    左闭右闭 [left, right] --
        因为定义target在[left, right]区间，所以有如下两点：

        while (left <= right) 要使用 <= ，因为 left == right 是有意义的，所以使用 <=
        if (nums[middle] > target) right 要赋值为 middle - 1，因为当前这个nums[middle]一定不是target，那么接下来要查找的左区间结束下标位置就是 middle - 1


    左闭右开 [left, right) --
        有如下两点：

        while (left < right)，这里使用 < ,因为left == right在区间[left, right)是没有意义的
        if (nums[middle] > target) right 更新为 middle，因为当前nums[middle]不等于target，去左区间继续寻找，
        而寻找区间是左闭右开区间，所以right更新为middle，即：下一个查询区间不会去比较 nums[middle]

参考链接:

https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html#_704-%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE


"""


# 以题目704为例

# 左闭右闭 [left, right]
def search1(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] < target:
            left = middle + 1
        elif nums[middle] > target:
            right = middle - 1
        else:
            return middle
    return -1


# 左闭右开 [left, right)
def search2(nums, target):
    if nums is None or len(nums) == 0:
        return -1
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = round(l + (r - l) / 2)
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1
