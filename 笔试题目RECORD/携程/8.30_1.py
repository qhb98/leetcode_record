

"""
携程的笔试是10道单选题 加 4道编程题, 其中3道力扣, 一道sql题

"""


"""

重排正整数的数位, 使得它变成偶数, 不能有前导0
一共有q次询问, 重排后可以和原数相等

输入:
    第一行输入一个正整数q, 代表询问次数
    后面的q行, 每行输入一个正整数x

输出:
    输出q行, 每行代表一次询问
    不存在合法解就直接输出-1

"""
import sys


def data_process(input_data):
    data_list = list(str(input_data))
    for idx in range(len(data_list)):
        num = int(data_list[idx])
        if num % 2 == 0:
            if data_list[-1] != "0":
                data_list[-1], data_list[idx] = data_list[idx], data_list[-1]
                res = int("".join(data_list))
                return res
            else:
                res = int("".join(data_list))
                return res
    return -1


if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        cur_data = input()
        data = data_process(cur_data)
        print(data)
    # input_list = list(map(int, input().split(" ")))
    # for i in range(1, q + 1):
    #     cur_data = input_list[i]
    #     data = data_process(cur_data)
    #     print(data)