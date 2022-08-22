# 先取出子序列, 再按照子序列从概率和数组中取数, 计算出结果append, 之后排序出最大值
# 贪心思想 不复习的题都是100*分数 那只要将小的那一部分都变成100的概率 那结果必然是最大的

def get_sub_sentences(rate_scores, maxi, scores):
    sub_sentences = []
    for i in range(maxi + 1):
        sub_sentences.append(sum(rate_scores[i:]) + sum(scores[:i]))
    sub_sentences.sort()
    return sub_sentences[-1]



def calculate(total_num, max_num, rates, scores):
    rate_score_list = []
    for i in range(total_num):
        rate_score_list.append(rates[i] * scores[i])
    rate_score_list.sort()
    sub_sentence = get_sub_sentences(rate_score_list, max_num, scores)
    return sub_sentence



def data_process(data_input):
    total_num, max_num = data_input[0][0], data_input[0][1]
    rates = [i/100 for i in data_input[1]]
    scores = data_input[2]
    result = calculate(total_num, max_num, rates, scores)
    return result


if __name__ == '__main__':
    data = []
    for i in range(3):
        data.append(list(map(int, input().split(' '))))
    res = data_process(data)
    print(res)