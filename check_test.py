# coding: utf-8
# @FileName: check_test.py
# @Time: 2022/8/1 22:09
# @Author: QHB


def generate_parenthesis(n):
    """
    题 22 括号生成
    方法: 回溯法
    :param n: int
    :return:List[str]
    """
    res = []
    back_tracking(n=n, result=res, left=0, right=0, s="")
    return res


def back_tracking(n, result, left, right, s):
    if right > left:
        return

    if left == n and right == n:
        result.append(s)
        return

    if left < n:
        back_tracking(n=n, result=result, left=left + 1, right=right, s=s + "(")

    if right < left:
        back_tracking(n=n, result=result, left=left, right=right + 1, s=s + ")")
