# coding: utf-8
# @FileName: test_509.py
# @Time: 2022/8/15 11:12
# @Author: QHB

# ========= 斐波那契数列 =========

# 1 确定dp table 以及下标的含义 dp[i] -- 第i个数的斐波那契数值是dp[i]
# 2 确定递推公式  即 状态转移方程 dp[i] = dp[i - 1] + dp[i - 2]
# 3 dp数组如何初始化 dp[0] = 0 dp[1] = 1
# 4 确定遍历顺序 dp[i] = dp[i - 1] + dp[i - 2]
# 5 举例推导dp数组

# 递归实现
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

