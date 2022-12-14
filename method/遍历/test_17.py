# coding: utf-8
# @FileName: test_17.py
# @Time: 2022/8/16 18:34
# @Author: QHB
import collections


digits = "23"
# 将相应的数字与字母对应起来
dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
       '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
# 首先初始化一个队列
q = collections.deque()
# 首先将数字字符串中的第一个数字压入到队列中
q.extend(dic[digits[0]])
# 将这个数字从字符串中移除，为了方便构建结束条件
digits = digits[1:]
# 当数字字符串不为空时，此时表示还需要有新的字母组合
while digits:
    # 因为每个数字对应的字母均要用来进行字母组合，所以这边需要知道每一层的字母个数
    for i in range(len(q)):
        # 首先将第一个元素弹出
        tmp = q.popleft()
        # 将第一个元素弹出，此时需要与第二个数字对应的字母进行组合，每个字母均需要，所以这边要按照长度进行遍历
        for j in range(len(dic[digits[0]])):
            # 将弹出的元素和新的字母进行组合
            tmp1 = tmp + dic[digits[0]][j]
            # 组合后放入队列中
            q.append(tmp1)
    # 将这个已经组合完成的数字移除
    digits = digits[1:]
# 因为刚刚元素均存在了队列中，此时需要返回一个数组，所以需要重新初始化一个数组
res = []
# 将队列中的每一个元素弹出，并放入到结果数组中
for p in range(len(q)):
    # 将队列中元素弹出
    tmp_pop = q.popleft()
    # 放入结果数组中
    res.append(tmp_pop)
# 返回结果即可
print(res)
