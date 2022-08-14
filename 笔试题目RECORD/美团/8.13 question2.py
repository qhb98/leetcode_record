# coding: utf-8
# @FileName: 8.13 question2.py
# @Time: 2022/8/14 14:34
# @Author: QHB

# 扫地机器人 求扫地机器人按照调度指令是否可以扫完一个二维的空间
# n*m的二维矩阵遍历的问题 medium题
# 输入 n m k \n len(str())=k

def direction_judge(i, j, direction):
    if direction == "S":
        return i, j - 1
    elif direction == "W":
        return i, j + 1
    elif direction == "A":
        return i - 1, j
    elif direction == "D":
        return i + 1, j


def move_func(n, m, k, directions):
    # 注意一下这里生成二维矩阵的方法 除了numpy之外, 这种方法也是可行的
    # 但是 [[0]*m]*n 后面不能给特定位置赋值, 会出问题
    room = [[0] * m for _ in range(n)]
    room[0][0] = 1
    # 统计当前走了多少步
    count = 0
    # 表示机器人当前的坐标位置
    cur_i, cur_j = 0, 0
    clean_count = 0
    for i in range(k):
        direction = directions[i]
        count += 1
        # 确定下一个坐标位置
        next_i, next_j = direction_judge(cur_i, cur_j, direction)
        room[next_i][next_j] = 1
        clean_count = 0
        if count >= n * m:
            for i in range(n):
                for j in range(m):
                    if room[i][j] == 0:
                        clean_count += 1
            if clean_count == 0:
                return "Yes", i + 1
    if clean_count > 0:
        return "No", clean_count


def str_2_data(input_data):
    split_res = input_data.split("\n")
    n = int(split_res[0].split(" ")[0])
    m = int(split_res[0].split(" ")[1])
    k = int(split_res[0].split(" ")[2])
    directions = list(split_res[1])
    res1, res2 = move_func(n, m, k, directions)
    return res1, res2


if __name__ == '__main__':
    input_data = "2 2 5\nSDWAS"
    result1, result2 = str_2_data(input_data)
    print(result1)
    print(result2)
