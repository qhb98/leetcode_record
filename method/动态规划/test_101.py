# coding: utf-8
# @FileName: test_101.py
# @Time: 2022/8/16 16:01
# @Author: QHB


# 剑指offer第101题  分割等和子集问题

def can_partition(nums):
    total = sum(nums)
    # 如果是奇数, 直接返回False
    if total % 2 != 0:
        return False
    bag = total // 2
    M = max(nums)
    # 如果最大值比均值还大, 说明其他值加起来小于均值, 也不可能True
    if bag < M:
        return False
    n = len(nums)
    dp = [True] + [False] * bag
    for i, num in enumerate(nums):
        for j in range(bag, num - 1, -1):
            dp[j] = dp[j] | dp[j - num]
    return dp[bag]


print(can_partition(nums=[1, 5, 11, 5]))
