# 3．马尔可夫文本分析和应用
# (1）马尔可夫文本分析计算文本中单词组合和其后续单词（含标点符号）的映射，这个单词组合被称为马尔可夫分析的前缀，
# 前缀中单词的个数被称为马尔可夫分析的“阶数”。编写 Python 代码实现某个文本的 n 阶马尔可夫文本分析，并且将分析结果记录在字典中。
# （2）采用（1）所实现的马尔可夫分析模块，对“emma.txt”或“whitefang.txt”进行马尔可夫分析，
# 运用 n 阶马尔可夫分析的结果生成由 m 个句子（注意首字母大写和结尾标点符号）组成的随机文本。
# 分析所生成文本的语义自然性和阶数n 的关系。
# （3）尝试采用 Python 不同的序列数据结构表示前缀，比较运行效率的差异。


# n阶就是定位到单词x后n个单词，统计这些n个单词在x后出现的概率，

# 首先找到所有单词和标点符号，放在一个列表中

# 再转化成一个字典（不包含标点符号）

# 在列表中查找字典中每个元素，到其后缀出现的概率
# 【首单词 = {后缀1：概率，后缀二：概率}。。。。。。】

from time import time
import json


# 首先找到所有单词和标点符号，放在一个列表中
def PreProcess():
    list1 = open("whitefang.txt").read().split()  # 按顺序存储原始文本所有单词包括标点符号
    list2 = open("emma.txt").read().split()
    wordlist = list1 + list2
    return wordlist, set(wordlist)  # 将wordlist转化为集合


# 在列表中查找字典中每个元素，到其后缀出现的概率
# 【首单词 = {后缀1：概率，后缀二：概率}。。。。。。】
def markov_analysis(n):
    wordlist, wordset = PreProcess()
    result = dict()  # { 单词：{后缀：概率。。。。}。。。。。。}
    for i in wordset:
        # 元素i,收集在wordlist中后n个元素出现概率返回一个字典{后缀1：概率，后缀2：概率。。。。}
        if i not in result:
            result[i] = marcov_find(i, wordlist, n)
    return result


def marcov_getstr(t):
    temp = ""
    for i in t:
        temp += i + " "
    return temp[0:-1]


def marcov_find(key, wordlist, n):
    result = {}
    for i in range(len(wordlist) - n):
        if key == wordlist[i]:
            temp = marcov_getstr(wordlist[i + 1:i + 1 + n])
            result[temp] = result[temp] + 1 if temp in result else 1
    SUM = sum(result.values())
    for i in result.keys():
        result[i] /= SUM
    return result


def writeresult(result):
    jsObj = json.dumps(result)
    fileObject = open(r'result.json', 'w')
    fileObject.write(jsObj)
    fileObject.close()


if __name__ == "__main__":
    tt = time()
    writeresult(markov_analysis(1))
    print(time() - tt)
