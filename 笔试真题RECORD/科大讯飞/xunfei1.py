# 1/2 开始的序列, 求前n项的和

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 求取指定长度序列的和
# @param n int整型 序列长度
# @return float
def seqSum(n):
    current_fen_zi = 1
    current_fen_mu = 2
    num = current_fen_zi / current_fen_mu
    if n == 1:
        print(float(num))
    else:
        res = []
        res.append(num)
        for i in range(2, n):
            next_fen_mu = current_fen_zi + current_fen_mu
            next_fen_zi = current_fen_mu
            num = next_fen_zi / next_fen_mu
            res.append(num)
            current_fen_mu = next_fen_mu
            current_fen_zi = next_fen_zi
        print(float('%0.2f'%sum(res)))