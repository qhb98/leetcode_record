# coding: utf-8
# @FileName: check_test.py
# @Time: 2022/8/1 22:09
# @Author: QHB

# def merge(intervals):
# 	"""
# 	题 56 合并区间
# 	排序法
# 	:param intervals: List[List[int]]
# 	:return: List[List[int]]
# 	"""
# 	# 考虑边界条件
# 	if intervals is None or len(intervals) == 1:
# 		return intervals
# 	res = []
# 	# 对intervals 进行排序
# 	intervals.sort(key=lambda x: x[0])
# 	print("排序后的结果:  ", intervals)
# 	for interval in intervals:
# 		if len(res) == 0 or interval[0] >res[-1][1]:
# 			res.append(interval)
# 		else:
# 			res[-1][1] = max(res[-1][1], interval[1])
# 	return res
#
#
# print(merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))


# def insert2(intervals, new_interval):
# 	"""
# 	题57  插入区间
# 	解法  贪心算法
# 	:param intervals: List[List[int]]
# 	:param new_interval:  List[int]
# 	:return: List[List[int]]
# 	"""
# 	res = []
# 	# 先考虑边界条件
# 	if intervals is None or new_interval is None:
# 		return intervals or new_interval
# 	if len(intervals) == 0:
# 		res.append(new_interval)
# 		return res
# 	elif len(new_interval) == 0:
# 		return intervals
# 	intervals.append(new_interval)
# 	# 先排序
# 	intervals.sort(key=lambda x: x[0])
# 	for interval in intervals:
# 		if len(res) == 0 or res[-1][1] < interval[0]:
# 			res.append(interval)
# 		else:
# 			res[-1][1] = max(interval[1], res[-1][1])
# 	return res
#
#
# print(insert2(intervals=[[1, 3], [6, 9]], new_interval=[2, 5]))


def subsets(nums):
	"""
	题78  子集
	解法
	:param nums: List[int]
	:return:  List[List[int]]
	"""



print(subsets(nums=[1, 2, 3]))
