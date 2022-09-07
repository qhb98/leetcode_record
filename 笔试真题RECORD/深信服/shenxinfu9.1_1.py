
"""
深信服python后端开发岗的笔试是10道不定项选择题, 10道填空题, 两道编程题

不定项选择题主要考察了 进程 线程 python对象和类 数据库 等一些有关python的基础知识
填空题主要考察了 数据库事务 代码填空 等知识
编程题两道都做出来了, 但是正确率都只有90%, 也不知道哪儿少考虑了. 估计是什么边界条件没考虑到.


"""


"""
给定字符串, 分成若干子串, 判断输入的字符串是否是对称字符串
是True  否False

考察 栈

"""


def duichen_judge(data):
    # 边界条件 若字符串长度为1
    if len(data) == 1:
        return True
    queue = []
    for i in range(len(data)):
        if len(queue) == 0:
            queue.append(data[i])
        elif queue[-1] != data[i]:
            queue.append(data[i])
        elif queue[-1] == data[i]:
            queue.pop(-1)
    if len(queue) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    str_data = list(input())
    res = duichen_judge(str_data)
    print(res)
