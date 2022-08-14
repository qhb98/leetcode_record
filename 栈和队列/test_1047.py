# coding: utf-8
# @FileName: test_1047.py
# @Time: 2022/8/14 22:37
# @Author: QHB

# 删除字符串中的所有相邻重复项


def remove_duplicates(s):
    res = list()
    for item in s:
        if res and res[-1] == item:
            res.pop()
        else:
            res.append(item)
    # 字符串拼接
    return "".join(res)


print(remove_duplicates(s="abbaca"))
