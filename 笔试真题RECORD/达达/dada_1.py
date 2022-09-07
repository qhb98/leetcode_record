
"""

给定一个数组prices, 第i个元素prices[i]表示一支给定股票在第i天的价格.
只能选择 某一天 买入这只股票, 并重未来的某一个不同的日子卖出这个股票

设计算法计算所能获得的最大利润, 返回从这笔交易中获取的最大利润
如果不能获取利润, 就返回0

"""


def prices(nums):
    # 双指针
    if len(nums) <= 1:
        return 0
    if len(nums) == 2 and nums[0] >= nums[1]:
        return 0

    max_price = 0
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] > nums[right]:
            left += 1
        else:
            if nums[right] <= nums[right - 1]:
                max_price = max(max_price, nums[right] - nums[left])
                right -= 1
            else:
                max_price = max(max_price, nums[right] - nums[left])
                left += 1
    return max_price


if __name__ == '__main__':
    nums = input().split("[")[1]
    nums = nums.split("]")[0]
    nums = list(map(int, nums.split(",")))
    res = prices(nums)
    print(res)

# [7,2,5,1,3,6,4]
