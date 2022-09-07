
# 二维矩阵

def calculate(n, x, y, distance):
    results = []
    for i in range(max(1, x - distance), min(n + 1, x + distance)):
        for j in range(max(1, y - distance), min(n + 1, y + distance)):
            if abs(i - x) + abs(j - y) == distance:
                results.append((i, j))
    return results


def data_process(data_input):
    n = data_input[0][0]
    x1, y1 = data_input[1][0], data_input[1][1]
    x2, y2 = data_input[2][0], data_input[2][1]
    x3, y3 = data_input[3][0], data_input[3][1]
    dis1, dis2, dis3 = data_input[4][0], data_input[4][1], data_input[4][2]
    result1 = calculate(n, x1, y1, dis1)
    result2 = calculate(n, x2, y2, dis2)
    result3 = calculate(n, x3, y3, dis3)
    result = min(set(result1).intersection(set(result3), set(result2)))
    return result


if __name__ == '__main__':
    data = []
    for i in range(5):
        data.append(list(map(int, input().split(" "))))
    res = data_process(data)
    print(res[0], res[1])



