

"""

要求时间复杂度必须要小于O(N), 就需要充分利用折叠数组的概念去解题

存在一个无重复的升序数组nums, 在nums的下标k处进行折叠, 将前段折叠后拼到nums数组尾部,
使得数组变为 nums[k], nums[k+1], ..., nums[n-1], nums[0], ..., nums[k-1]

给定一个折叠后的nums数组, 和一个整数target, 如果nums中存在target, 则返回target所在的
下标, 否则返回-1

第一行为nums数组
第二行为target整数

"""

if __name__ == '__main__':
    nums = input()
    target = int(input())
    nums_st = int(nums.split(",")[0].split("[")[1])
    nums_ed = int(nums.split(",")[-1].split("]")[0])
    nums_center = list(map(int, nums.split(",")[1:-1]))
    nums_center.insert(0, nums_st)
    nums_center.append(nums_ed)
    nums = nums_center[:]
    if nums[0] > target > nums[-1]:
        print(-1)
    elif target == nums[0]:
        print(0)
    elif target == nums[-1]:
        print(len(nums) - 1)
    elif target < nums[-1]:
        for num in nums[-nums[-1]:]:
            if num == target:
                print(nums.index(num))
                break
        print(-1)
    elif target > nums[0]:
        for num in nums[1:-nums[-1]+1]:
            if num == target:
                print(nums.index(num))
                break
        print(-1)





