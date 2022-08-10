# coding: utf-8
# @FileName: :test_39.py
# @Time: 2022/8/9 21:48
# @Author: QHB

"""

回溯算法: 进行选择; 递归; 撤回选择

解决  排列问题  子集问题 组合问题  切割问题  棋盘问题(n皇后 解数独)

    void backtracking(parameters){
         if (终止条件) {
            收集结果
            return
         }

         # 进入单层搜索的逻辑
         for (集合的元素){
            处理节点
            递归函数
            回溯操作 -- 撤销处理节点的情况
         }
         return

    }

参考学习链接:
https://www.bilibili.com/video/BV1cy4y167mM?spm_id_from=333.337.search-card.all.click&vd_source=7111d4cfa9354342c253c06ecdd64e2f

"""


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
        return

    for j in range(candidates.index(cur), len(candidates)):
        cur_sum += candidates[j]
        cur_result.append(candidates[j])
        backtrack(cur=candidates[j], candidates=candidates, res=res, target=target, cur_result=cur_result,
                  cur_sum=cur_sum)
        cur_sum -= candidates[j]
        cur_result.pop()


s_sum = combination_sum(candidates=[2, 3, 6, 7], target=7)
print(s_sum)
