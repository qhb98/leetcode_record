# coding: utf-8
# @FileName: :test_39.py
# @Time: 2022/8/9 21:48
# @Author: QHB


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
        backtrack(i, tmp_sum=candidates[i], tmp=[candidates[i]], res=res, target=target, candidates=candidates)
    return res


def backtrack(i, tmp_sum, tmp, res, target, candidates):
    if tmp_sum > target or i >= len(candidates):
        tmp.pop()
        return

    if tmp_sum == target:
        res.append(tmp)
        return

    for j in range(i, len(candidates)):
        if tmp_sum + candidates[j] > target:
            break
        tmp.append(candidates[j])
        backtrack(j, tmp_sum=tmp_sum + candidates[j], tmp=tmp, res=res, target=target, candidates=candidates)
        tmp.pop()
        tmp_sum = tmp_sum - candidates[j]


s_sum = combination_sum(candidates=[2, 3, 6, 7], target=7)
print(s_sum)
