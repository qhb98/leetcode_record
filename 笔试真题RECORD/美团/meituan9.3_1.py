"""
输入 a b 两个整数 a <= a,b <= 99

要求a >= 11 或者 a - b >=2 才能胜利

"""


def bijiao(a, b):
    # 如果a小于11并且b小于等于9, 那么只要达到11就可以了
    if a < 11 and b <= 9:
        return 11 - a

    # 如果a小于11, 但是b大于9 小于11
    if a < 11 and 9 < b < 11:
        return 11 - a + 2 - (11 - b)

    # 如果b大于等于11
    if b >= 11:
        return b + 2 - a


if __name__ == '__main__':
    ab = list(map(int, input().split(" ")))
    a, b = ab[0], ab[1]
    res = bijiao(a, b)
    print(res)
