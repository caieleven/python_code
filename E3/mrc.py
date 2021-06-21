#from E3.Marcov_Analysis import marcov_find
from random import randint
import re

class Markov:
    @classmethod
    #read and store
    def RSfile(cls):
        with open("D:\\codefile\\python_code\\E3\\emma.txt") as file:
            text = file.read()
            text = re.sub(r'[\s *\[\]#-]+', ' ', str(text))
        punctuation = [',', '.', ';',':','?', '!']
        for symbol in punctuation:
            text = text.replace(symbol, ""+symbol+" ")
        words = text.split(" ")
        words = [word for word in words if word != '']
        cls.__wordslist = words


    @staticmethod
    def CalculateSum(wordsdict):
        sum = 0
        for val in wordsdict.values():
            sum += val
        return sum
    
    def returnRandomword(self, key):
        flag = True
        while(flag):
            randomindex = randint(1, Markov.CalculateSum(self.__wordsdic[key]))
            for kk, num in self.__wordsdic[key].items():
                if randomindex - num <= 0:
                    flag = False
                    returnval = kk
                    break
        return returnval


    def __init__(self, n):
        self.__n = n
        self.__wordsdic = {}

    def get_n(self):
        return self.__n


#可以用迭代器（生成器？）来改进
    def InitWordsDict(self):
        for start in range(len(Markov.__wordslist) - self.__n):
            #选取连续的n个单词为key
            #列表不可哈希，不可作为key，需转换
            key = ''
            for word in Markov.__wordslist[start:start+self.__n]:
                key += word + ' '
            valindex = start+self.__n
            if key not in self.__wordsdic:
                self.__wordsdic[key] = {}
            if Markov.__wordslist[valindex] not in self.__wordsdic[key]:
                self.__wordsdic[key][Markov.__wordslist[valindex]] = 0
            self.__wordsdic[key][Markov.__wordslist[valindex]] += 1

    def GeneChain(self):
        self.InitWordsDict()
        #currentkey = "The fifty hours "
        currentkey = self.GeneTheFirst()
        chain = currentkey
        count = 0
        mark = {'.', '?', '!'}
        while count <= 10:
            newword = self.returnRandomword(currentkey)
            if newword[len(newword) - 1] in mark:
                count += 1
            chain+=(newword + " ")
            currentkey =currentkey.split(' ', 1)[1] + newword + ' '
        
        print(chain)

    def GeneTheFirst(self):
        index = randint(1, 100000)
        flag = True
        mark = {'.', '?', '!'}
        firstkey = ""
        #找到一个句子开始的单词
        while flag:
            Firstword = self.__wordslist[index]
            if Firstword[len(Firstword)-1] in mark:
                if 'A' <=self.__wordslist[index + 1][0] <= 'Z':
                    flag = False
            index += 1
        for i in range(self.__n):
            firstkey += self.__wordslist[index] + ' '
            index += 1
        return firstkey







if __name__ == '__main__':
    Markov.RSfile()
    sss = Markov(3)
    sss.GeneChain()    


