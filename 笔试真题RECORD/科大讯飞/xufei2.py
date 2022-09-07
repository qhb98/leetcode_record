#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 验证指令的正确性
# @param signal string字符串 待验证的指令
# @return bool布尔型
#
def signalVerify(signal: str):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    str_small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"
                 , "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    type = list(signal.split("="))[0]
    value = list(signal.split("="))[1]
    value_list = list(value)
    if value_list[0] == " ":
        print(False)
    for v in value_list:
        if v not in numbers and v != " " and v not in str_small:
            print(True)
    print(value)

signalVerify(input())