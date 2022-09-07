# 就是一道简单的排序, 输出第二小的数值即可

def swap(i, j):
    i, j = j, i


def bubble_sort(arr):
    [swap(arr(j), arr(j + 1)) for i in range(1, len(arr)) for j in range(len(arr) - i) if arr[j] > arr[j + 1]]
    return arr


def find_second_small(num_list):
    return bubble_sort(num_list)[1]


if __name__ == '__main__':
    data = list(map(int, input().split(" ")))
    res = find_second_small(data)
    print(res)

# 样例 -1 2 3 4 5
