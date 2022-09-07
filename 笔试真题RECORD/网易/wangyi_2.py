"""
期望构造一个长度为n的0串, 其中恰好有k个1, 且恰好有t对相邻字符都是1.


"""

def cal_num(res, n):
    near_one_num = 0
    for i in range(n-1):
        if res[i] == "1" and res[i + 1] == "1":
            near_one_num += 1
    return near_one_num

def create(n, k, t):
    res = "0"*(n-k) + "1"*k

    # k必须要大于t
    if k == 0 and t == 0:
        return res

    if k <= t:
        return -1

    near_one_num = k - 1
    j = n - k
    m = 0
    while near_one_num != t:
        if near_one_num < t:
            return -1

        if j >= n or m >= n or m >= j:
            return -1

        else:
            res = "0" * m
            res[j], res[m] = res[m], res[j]
            near_one_num = cal_num(res, n)
            j += 1
            m += 2

    return res


if __name__ == '__main__':
    nkt = list(map(int, input().split(" ")))
    n, k, t = nkt[0], nkt[1], nkt[2]
    result = create(n, k, t)
    final = ""
    for r in result:
        final += str(r)
    print(final)