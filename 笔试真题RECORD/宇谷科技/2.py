# coding: utf-8
# @FileName: 2.py
# @Time: 2022/9/2 19:18
# @Author: QHB

"""
A = m * n 矩阵
B = n * p 矩阵

A*B = C
return C

"""


def matrix_multi(a, b):
    ## 考虑边界条件
    # 如果不满足a的列数等于b的行数
    if len(a[0]) != len(b):
        return -1

    # 如果某个矩阵为空
    if (len(a) == 0 and len(a[0]) == 0) or (len(b) == 0 and len(b[0]) == 0):
        return -1

    # 正常情况
    a_row = len(a)
    col = len(a[0])
    b_col = len(b[0])

    c = [[0] * b_col for _ in range(a_row)]
    for i in range(a_row):
        for k in range(b_col):
            sum_ = 0
            for j in range(col):
                sum_ += a[i][j] * b[j][k]
            c[i][k] = sum_

    return c


if __name__ == '__main__':
    A = [
        [1, 2],
        [3, 4]
    ]
    B = [
        [2, 2, 3],
        [2, 2, 4]
    ]
    C = matrix_multi(A, B)
    print(C)
