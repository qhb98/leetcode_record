# coding: utf-8
# @FileName: test_239.py
# @Time: 2022/8/14 22:48
# @Author: QHB

# 滑动窗口最大值


class MyQueue:  # 单调队列 从大到小
    def __init__(self):
        self.queue = []  # 使用list来实现单调队列

    # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    # 同时pop之前判断队列当前是否为空。
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0)
            # list.pop()时间复杂度为O(n),这里可以使用collections.deque()

    # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    # 这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    # 查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
    def front(self):
        return self.queue[0]


def slide_window(nums, k):
    que = MyQueue()
    result = []
    for i in range(k):  # 先将前k的元素放进队列
        que.push(nums[i])
    result.append(que.front())  # result 记录前k的元素的最大值
    for i in range(k, len(nums)):
        que.pop(nums[i - k])  # 滑动窗口移除最前面元素
        que.push(nums[i])  # 滑动窗口前加入最后面的元素
        result.append(que.front())  # 记录对应的最大值
    return result


def my_slide_window(nums, k):
    res = []
    for i in range(len(nums) - k + 1):
        window = nums[i:k+i]
        res.append(max(window))
    return res


print(slide_window(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(my_slide_window(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
