def winMazeGift(maze):
    final_pos = [(i, j) for i in range(len(maze)) for j in range(len(maze[0])) if maze[i][j] == 8][0]
    pos_x = final_pos[0]
    pos_y = final_pos[1]
    can_moves = []
    backtracking(maze, pos_x, pos_y, can_moves, res=[])


def backtracking(maze, pos_x, pos_y, can_moves, res):
    if pos_x == 0 or pos_x == 3 or pos_y == 0 or pos_y == 3:
        res.append(can_moves)
        return

    while pos_x != 0 or pos_x != 3 or pos_y != 0 or pos_y != 3:
        for i in range(pos_x - 1, pos_x + 1):
            for j in range(pos_y - 1, pos_y + 1):
                if maze[pos_x][pos_y] == 0:
                    can_moves.append((i, j))
                    pos_x = i
                    pos_y = j


winMazeGift([[0,1,1,1],[0,0,0,1],[1,0,8,1],[1,0,1,1]])