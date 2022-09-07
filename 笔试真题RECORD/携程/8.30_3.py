"""
有n个数字的数列
平滑值: 任意两个相邻的数的差点绝对值的最大值

在只修改一个位置的数字, 可以修改为任意值, 或者不修改的情况下, 数列的平滑值最小是多少

输入:
    第一行数字n表示数列的长度
    第二行数列a



"""


def data_process(n, a):
    res = 0
    cur = 0
    if n == 2:
        return res
    # 三指针
    pre_k = 0
    cur_k = 1
    aft_k = 2
    for i in range(n - 2):
        delta1 = abs(a[cur_k] - a[pre_k])
        delta2 = abs(a[cur_k] - a[aft_k])
        if delta1 > res or delta2 > res:
            res = max(delta1, delta2)
            cur = cur_k
    a[cur] = (a[cur - 1] + a[cur + 1]) // 2
    res = max(abs(a[cur - 1] - a[cur]), abs(a[cur + 1] - a[cur]))
    return res


if __name__ == '__main__':
    n = int(input().split("\n")[0])
    a = [int(i) for i in input().split(" ")]
    res = data_process(n, a)
