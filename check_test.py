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

def merge(s1, s2, s):
	"""
	将两个列表按顺序融合为一个列表
	:param s1:
	:param s2:
	:param s:
	:return:
	"""
	i = j = 0
	while i + j < len(s):
		if j == len(s2) or i < len(s1) and s1[i] < s2[j]:
			s[i+j] = s1[i]
			i += 1
		else:
			s[i+j] = s2[j]
			j += 1


def merge_sort(s):
	"""
	归并排序
	:param s:
	:return:
	"""
	n = len(s)
	# 剩一个或者没有直接返回, 不用排序
	if n < 2:
		return
	# 拆分
	mid = n // 2
	s1 = s[0:mid]
	s2 = s[mid:n]
	merge_sort(s1)
	merge_sort(s2)
	# 合并
	merge(s1, s2, s)


if __name__ == '__main__':
	s = [7, 8, 4, 1, 6, 5, 2, 3]
	merge_sort(s)
	print(s)