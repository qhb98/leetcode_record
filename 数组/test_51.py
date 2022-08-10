# coding: utf-8
# @FileName: :test_51.py
# @Time: 2022/8/10 15:26
# @Author: QHB

"""
参考思路链接:

https://programmercarl.com/0051.N%E7%9A%87%E5%90%8E.html#%E6%80%9D%E8%B7%AF

"""


def solve_n_queens(n):
    if not n:
        return []
    board = [['.'] * n for _ in range(n)]
    res = []

    def is_valid(board, row, col):
        # 判断同一列是否冲突
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False
        # 判断左上角是否冲突
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 判断右上角是否冲突
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def backtracking(board, row, n):
        # 如果走到最后一行，说明已经找到一个解
        if row == n:
            temp_res = []
            for temp in board:
                temp_str = "".join(temp)
                temp_res.append(temp_str)
            res.append(temp_res)
        for col in range(n):
            if not is_valid(board, row, col):
                continue
            board[row][col] = 'Q'
            backtracking(board, row + 1, n)
            board[row][col] = '.'

    backtracking(board, 0, n)
    return res


print(solve_n_queens(4))
