"""

小红拿到了一个数组, 每次进行如下操作:
任选一个数, 使其加k, 进行任意次这样的操作, 最终数组最多有多少个数相同

第一行输入两个正整数n k, 分别代表数组的长度和每次加的数值
第二行输入n个正整数, 表示拿到的数组

"""


def same_num_max(n, k, nums):
    num_list = [0] * n
    nums = sorted(nums)
    for i in range(n):
        for j in range(n):
            if i != j:
                if (nums[j] - nums[i]) % k == 0:
                    num_list[i] += 1
    return max(num_list) + 1


if __name__ == '__main__':
    n = 5
    k = 2
    second_row = [5, 1, 2, 3, 5]
    # first_row = list(map(int, input().split(" ")))
    # n, k = first_row[0], first_row[1]
    # second_row = list(map(int, input().split(" ")))
    res = same_num_max(n, k, second_row)
    print(res)
