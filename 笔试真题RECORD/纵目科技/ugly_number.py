# coding: utf-8
# @FileName: ugly_number.py
# @Time: 2022/9/3 14:08
# @Author: QHB

"""

纵目科技是一家做自动驾驶的公司, 这家公司很恶心, 发的是测评的邮件, 结果进去后发现是6道力扣的编程题,
笔试变成了测评, 估计是 不想招人, 还只给了90分钟, 巨离谱

"""

"""

我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
这是一道由分解质因数改编过来的题目, 没准备过类似的, 所以当时没写出来

https://leetcode.cn/problems/chou-shu-lcof/

思路:
    丑数的递推性质: 丑数只包含因子2 3 5, 因此可以推导出 丑数 = 某较小丑数 × 某因子
    
    设已知长度为n的丑数序列x_1 x_2 ... x_n, 求第n+1个丑数 x_n+1. 根据递推性质, 丑数 x_n+1 只可能是以下三种
    情况的其中之一.
    x_n+1 = x_a * 2 or x_b * 3 or x_c * 5 
    
    所以可以得到丑数的递推公式: x_n+1 = min(x_a * 2, x_b * 3, x_c * 5)
    
    因此可以设置指针a b c指向首个丑数, 即1, 循环根据递推公式得到下个丑数, 并且每轮将对应指针执行+1即可.
    动态规划解析:
        状态定义: 设动态规划列表dp, dp[i]代表第i+1个丑数
        转移方程: 
            [1] 当索引a b c满足以下条件时, dp[i]为三种情况的最小值
            [2] 每轮计算dp[i]后, 需要更新索引a b c的值, 使其始终满足方程条件. 
        初始状态:
            dp[0] = 1
        返回值:
            dp[n-1]
        
"""


# ========================== 来源于剑指offer49.丑数 ===========================

def count_ugly(n):
    dp, a, b, c = [1] * n, 0, 0, 0
    for i in range(1, n):
        n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
        dp[i] = min(n2, n3, n5)
        if dp[i] == n2:
            a += 1
        if dp[i] == n3:
            b += 1
        if dp[i] == n5:
            c += 1
    return dp[-1]


# ========================== 判断是否是丑数 ===========================
def is_ugly(n):
    if n < 1:
        return False
    while n % 2 == 0:
        n /= 2
    while n % 3 == 0:
        n /= 3
    while n % 5 == 0:
        n /= 5
    if n == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    print(count_ugly(n=5))
    print(is_ugly(n=5))
