# coding: utf-8
# @FileName: :greedy_algorithm.py
# @Time: 2022/8/10 21:44
# @Author: QHB

"""

贪心算法:  想清楚局部最优，想清楚全局最优，感觉局部最优是可以推出全局最优，并想不出反例，那么就试一试贪心

"""


# 以题455为例

# 思路1 -- 优先考虑喂饼干

def find_content_children1(g, s):
    g.sort()
    s.sort()
    res = 0
    for i in range(len(s)):
        if res < len(g) and s[i] >= g[res]:
            # 小饼干先喂饱小胃口
            res += 1
    return res


# 思路2 -- 优先考虑胃口

def find_content_children2(g, s):
    g.sort()
    s.sort()
    start, count = len(s) - 1, 0
    for index in range(len(g) - 1, -1, -1):
        # 先喂饱大胃口
        if start >= 0 and g[index] <= s[start]:
            start -= 1
            count += 1
    return count
