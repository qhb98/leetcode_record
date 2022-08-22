
# 字符串按顺序拼接

def combine(length, a_list, b_list):
    combine_res = ""
    for i in range(length):
        combine_res += a_list[i] + b_list[i]
    return combine_res


def data_process(input):
    length = int(input[0][0])
    a_list = list(input[1][0])
    b_list = list(input[2][0])
    result = combine(length, a_list, b_list)
    return result


if __name__ == '__main__':
    data = []
    for i in range(3):
        data.append(list(map(str, input().split(" "))))
    res = data_process(data)
    print(res)
