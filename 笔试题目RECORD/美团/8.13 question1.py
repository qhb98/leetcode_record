# coding: utf-8
# @FileName: 8.13 question1.py
# @Time: 2022/8/14 14:33
# @Author: QHB


# 魔法外卖 求订单没有按时送到的次数 easy题
# 输入
# 第一行 正整数 n个订单 每笔订单需要消耗的时间t
# 第二行 n个订单的截止送达时间

# 输出 需要使用的魔法次数


def orders_cal(n, t, orders):
    count = 0
    can_count = 0
    pre_order = 0
    for cur_order in orders:
        # 如果两笔订单之间的时间差超过需要耗时, 说明可以送到
        if cur_order - pre_order >= t:
            can_count += 1
            pre_order = t * can_count
        else:
            # 否则送不到
            count += 1
    return count


def sys_process(input):
    # 输入的第一行处理
    inputed_res = input.split("\\n")
    n = int(inputed_res[0].split(" ")[0])
    t = int(inputed_res[0].split(" ")[1])
    orders = [int(i) for i in inputed_res[1].split(" ")]
    result = orders_cal(n, t, orders)
    return result


if __name__ == '__main__':
    # input_data = "6 5\n100 101 102 103 104 105"
    # input_data = "6 5\n5 6 7 8 9 10"
    input_data = input()
    res = sys_process(input_data)
    print(res)
