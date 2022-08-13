# coding: utf-8
# @FileName: :test_376.py
# @Time: 2022/8/13 10:06
# @Author: QHB

# 第 376 题 摆动序列

def wiggle_max_length(nums):
    # 题目里nums长度大于等于1, 当长度为1时, 其实到不了for循环里去, 所以不用考虑nums长度
    pre_c, cur_c, res = 0, 0, 1
    for i in range(len(nums) - 1):
        cur_c = nums[i + 1] - nums[i]
        # 差值为0时, 不算摆动
        if cur_c * pre_c <= 0 and cur_c != 0:
            res += 1
            # 如果当前差值和上一个差值为一正一负时, 才需要用当前差值替代上一个差值
            pre_c = cur_c
    return res


print(wiggle_max_length(nums=[1, 7, 4, 9, 2, 5]))
