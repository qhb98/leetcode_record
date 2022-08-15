# coding: utf-8
# @FileName: test_718.py
# @Time: 2022/8/15 22:33
# @Author: QHB

# 最长重复子数组


# 确定dp table以及下标的含义 dp[i][j]

A = [1, 2, 3, 2, 1]
B = [3, 2, 1, 4, 7]
res = 0
dp_table = [[0] * len(A) for _ in range(len(B))]
dp_table[0][0] = 0
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            dp_table[i][j] = dp_table[i - 1][j - 1] + 1
            if dp_table[i][j] > res:
                res = dp_table[i][j]
print(res)



