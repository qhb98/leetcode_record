"""
给定两个字符串形式的非负整数num1 和 num2, 计算他们的和, 并且同样以字符串形式返回

不能使用内置的加减乘除
不能直接将输入的字符串转换为整数形式

就是 力扣第 415 题

"""


def str_adding(num1, num2):
    res = ""
    i, j, carry = len(num1) - 1, len(num2) - 1, 0

    while i >= 0 or j >= 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0

        tmp = n1 + n2 + carry
        carry = tmp // 10

        res = str(tmp % 10) + res
        i -= 1
        j -= 1

    return "1" + res if carry else res


if __name__ == '__main__':
    num = input().split(",")
    num1, num2 = num[0], num[1]
    result = str_adding(num1, num2)
    print(result)
