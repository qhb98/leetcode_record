# coding: utf-8
# @FileName: test_209.py
# @Time: 2022/8/16 18:12
# @Author: QHB


# 题209  长度最小的连续子数组, 返回其长度, 否则返回0
s = 7
nums = [2, 3, 1, 2, 4, 3]

# 先考虑边界条件
if nums is None or len(nums) == 0:
    print(0)
res = len(nums) + 1
total = 0
i, j = 0, 0
while j < len(nums):
    total += nums[j]
    j += 1
    while total >= s:
        res = min(res, j - i)
        total -= nums[i]
        i += 1
if res == (len(nums) + 1):
    print(0)
else:
    print(res)

