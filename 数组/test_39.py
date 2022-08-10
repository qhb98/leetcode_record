# coding: utf-8
# @FileName: :test_39.py
# @Time: 2022/8/9 21:48
# @Author: QHB
import time


def combination_sum(candidates, target):
    """
    组合总和
    回溯算法
    :param candidates: List[int]
    :param target: int
    :return: List[List[int]]
    """
    res = []
    candidates.sort()
    # 先考虑边界条件
    if candidates is None or target < min(candidates) or (len(candidates) == 1 and target % candidates[0] != 0):
        res.append([])
        return res

    for i in range(len(candidates)):
        backtrack(cur=candidates[i], candidates=candidates, res=res, target=target, cur_result=[candidates[i]],
                  cur_sum=candidates[i])
    return res


def backtrack(cur, candidates, res, target, cur_result, cur_sum):
    if cur_sum == target:
        res.append(cur_result[:])
        return

    if cur_sum > target or cur_sum + min(candidates) > target:
        # cur_sum + min(candidates) > target 剪枝操作
        return

    for j in range(candidates.index(cur), len(candidates)):
        cur_sum += candidates[j]
        cur_result.append(candidates[j])
        backtrack(cur=candidates[j], candidates=candidates, res=res, target=target, cur_result=cur_result,
                  cur_sum=cur_sum)
        cur_sum -= candidates[j]
        cur_result.pop()


start_time = time.time()
for i in range(100):
    s_sum = combination_sum(candidates=[2, 3, 6, 7], target=7)
end_time = time.time()
print(end_time - start_time)
