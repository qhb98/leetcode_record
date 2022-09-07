"""
S表示一个非负整数集合, mex(S)的值为不属于集合S的最小非负整数.

有n个互不相同都非负整数a1 a2 ... an构成了一个非负整数集合A. 小美想知道若将ai从集合A中删除,
剩下的n-1个数构成的新集合A'的mex值为多少
输出i从1到n的所有取值下新集合的mex值

第一行输入一个整数n, 表示集合A的大小
第二行输入n个整数a1 a2 ... an

输出n个整数
"""


def mex(nums):
    result = 0
    for num in sorted(nums):
        if num == result:
            result = num + 1
    return result


if __name__ == '__main__':
    n = int(input())
    a_list = list(map(int, input().split(" ")))
    res = []
    for i in range(n):
        new_nums = a_list[:i] + a_list[i + 1:n]
        res.append(str(mex(new_nums)))
    print(" ".join(res))
