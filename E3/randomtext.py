import json
from random import randint
from random import random



def randomtext(result, n):
    pre = list(result.keys())[randint(0, len(result))]
    print(pre, end=" ")  # 随机获得一个开头
    while n >= 0 or pre[-1] != '.':
        predict = result[pre]
        Outstring = randomtext_nextword(predict)  # 根据概率随机获得一种后续组合
        print(Outstring, end=" ")
        pre = Outstring.split()[-1]
        n -= 1


def randomtext_nextword(predict):
    ranP = random()
    sum = 0
    for i in predict.keys():
        sum += predict[i]
        if ranP < sum:
            return i


if __name__ == "__main__":
    with open("result.json", 'r') as load_f:
        result = json.load(load_f)
    randomtext(result, 100)
