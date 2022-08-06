# coding: utf-8
# @FileName: :test_11.py
# @Time: 2022/8/6 21:18
# @Author: QHB

"""
力扣第11题, 乘最多水的容器
"""


def max_water1(input_arr):
    """
    双指针法遍历, 只要保证 max((end - start) * min(height[start], height[end])) 即可
    :param input_arr:
    :return:
    """
    # 首先考虑边界条件
    if input_arr is None or len(input_arr) <= 1:
        return 0
    elif len(input_arr) == 2:
        return min(input_arr[0], input_arr[-1])
    else:
        start = 0
        end = len(input_arr) - 1
        res = 0
        while start < end:
            res = max(res, (end - start) * min(input_arr[start], input_arr[end]))
            if input_arr[start] < input_arr[end]:
                start += 1
            else:
                end -= 1
        return res


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    final_res = max_water1(height)
    print(final_res)
