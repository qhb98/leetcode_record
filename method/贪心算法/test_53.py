# coding: utf-8
# @FileName: test_53.py
# @Time: 2022/8/13 10:19
# @Author: QHB

# 第 53 题 最大子序和

def max_sub_array(nums):
    cur_sum = 0
    count = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        count += 1
        if cur_sum < 0 and nums[i] > 0:
            cur_sum = nums[i]
            count = 1
        elif cur_sum < 0 and nums[i] < 0:
            cur_sum = 0
            count = 0
    return count


print(max_sub_array(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
