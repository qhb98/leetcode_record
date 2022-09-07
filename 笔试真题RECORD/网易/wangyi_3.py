"""
小红拿到了一个数组, 每次选择一个数, 使其减去x, 希望k次操作之后, 该数组的最大值尽可能小

第一行输入三个正整数n, k ,x, 代表数组的长度, 操作次数, 每次操作减去的数
第二行输入n个正整数, 表示数组

"""


def bubble_sort(n, nums):
    for i in range(1, n):
        for j in range(n-1):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def small_possible(n, k, x, nums):
    new_nums = bubble_sort(n, nums)
    skill = n - 1
    while k > 0:
        if new_nums[skill] >= new_nums[skill - 1]:
            new_nums[skill] -= x
            k -= 1
        else:
            new_nums = bubble_sort(n, new_nums)
            skill = n - 1

    return max(new_nums)


if __name__ == '__main__':
    # nkx = list(map(int, input().split(" ")))
    # n, k, x = nkx[0], nkx[1], nkx[2]
    # nums = list(map(int, input().split(" ")))
    n, k, x = 5, 3, 5
    nums = [4, 3, 11, 2, 1]
    result = small_possible(n, k, x, nums)
    print(result)
