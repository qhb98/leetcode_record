# coding: utf-8
# @FileName: 2.py
# @Time: 2022/9/1 14:11
# @Author: QHB

"""
有个大型的仓库使用拣货机器人从不同的货架间取货, 已知：
    1. 货架呈二维网格排列, 网格中的每个货架只会放置一种商品
    2. 受这代设备的技术水平所限, 机器人只能沿上下左右四个方向移动, 还不能沿着斜线移动清理

仓库当前使用的拣货算法是这样:
    1. 一张订单会包含x种商品, 分布在x个货架上
    2. 结合将这X种商品的所在位置, 将地图上的商品分解为Y个商品堆, 然后同时派出Y个机器人, 并发取货, 每个机器人只负责一个商品堆
    3. 商品堆的定义是上下左右彼此相邻的一组商品

在订单被分析后, 给你个由1和0组成的二维网格表示货架地图, 请计算需要派出的机器人的数量

# 核心: 其实就是 力扣上的岛屿问题 的相同解法

"""


def rec(i, j):
    """
    递归函数解决
    DFS深度优先搜索

    :param i: 当前所在网格的i坐标
    :param j: 当前所在网格的j坐标
    :return:
    """
    # 终止条件
    if i < 0 or j < 0 or i >= row or j >= col:
        return
    if visited[i][j] == 0 or matrix[i][j] == 0:
        return
    # 处理过程
    visited[i][j] = True

    # 递归方向
    rec(i + 1, j)
    rec(i, j + 1)
    rec(i - 1, j)
    rec(i, j - 1)


if __name__ == '__main__':
    grid = [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    row = len(grid)
    col = len(grid[0])
    visited = [[]]
    matrix = [[]]
    for i in range(row):
        for j in range(col):
            rec(i, j)
