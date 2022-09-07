# coding: utf-8
# @FileName: 1.py
# @Time: 2022/9/2 19:08
# @Author: QHB

def reserve_str(s):
    # 考虑边界条件
    if len(list(s)) <= 0:
        return -1

    new_s = []

    for i in range(1, len(list(s)) + 1):
        new_s.append(s[-i])
    new_s = "".join(new_s)

    return new_s


if __name__ == '__main__':
    s = "abcdef"
    res = reserve_str(s)
    print(res)
