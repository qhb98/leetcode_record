# coding: utf-8
# @FileName: devide_and_conquer.py
# @Time: 2022/8/15 22:49
# @Author: QHB


"""
分治算法 -- 就是把一个复杂的问题分成两个或更多的相同或相似的子问题，再把子问题分成更小的子问题……直到最后子问题可以简单的直接求解，原问题的解即子问题的解的合并

step 1 -- 将原问题分解为若干个规模较小、相互独立、与原问题形式相同的子问题
step 2 -- 若子问题规模较小而容易被解决则直接解, 否则递归解
step 3 -- 将各个子问题的解合并为原问题的解

"""


# LC 第 169 题 多数元素

def get_majority(nums, left, right):
    if left == right:
        return nums[left]

    mid = left + (right - left) // 2
    left_majority = get_majority(nums, left, mid)
    right_majority = get_majority(nums, mid + 1, right)

    if left_majority == right_majority:
        return left_majority
    else:
        left_count = 0
        right_count = 0
        for i in nums[left:right + 1]:
            if i == left_majority:
                left_count += 1
            elif i == right_majority:
                right_count += 1

        return left_majority if left_count > right_count else right_majority


print(get_majority(nums=[3, 2, 3], left=0, right=len([3, 2, 3]) - 1))
