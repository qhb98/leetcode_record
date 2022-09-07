"""
有a个"y", b个"o", c个"u", 用这些字母拼成一个字符串, 三个相邻的字母是you可以获得2分, 两个相邻的字母是oo可以获得1分

输入:
    第一行是一个整数q
    接下来q行, 每行3个正整数a b c 用空格隔开

"""


def data_process(a, b, c):
    reward = 0
    if b >= a and b >= c:
        you_num = min(a, c)
        reward += you_num * 2
        b -= you_num
        oo_num = max(0, b - 1)
        reward += oo_num
        return reward
    elif b <= a and b <= c:
        you_num = b
        reward += you_num * 2
        return reward
    elif b > a and b < c:
        you_num = a
        reward += you_num * 2
        b -= you_num
        oo_num = max(0, b - 1)
        reward += oo_num
        return reward
    elif b > c and b < a:
        you_num = c
        reward += you_num * 2
        b -= you_num
        oo_num = max(0, b - 1)
        reward += oo_num
        return reward
    else:
        you_num = b
        reward += you_num * 2
        return reward


if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        input_list = list(map(int, input().split(" ")))
        a, b, c = input_list[0], input_list[1], input_list[2]
        result = data_process(a, b, c)
        print(result)
