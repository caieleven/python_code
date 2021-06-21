import time

def read_file():
    global words_dic, maxlen, minlen
    file = open("D:\\codefile\\python_code\\E2\\words.txt")
    #得到单词长度范围
    for line in file:
        if maxlen < len(line.strip()):
            maxlen = len(line.strip())
        if minlen > len(line.strip()):
            minlen = len(line.strip())
    #初始化字典,注意其中创建空集合需要用set
    words_dic = {i:set() for i in range(1, maxlen + 1)}
    file.close()
    file = open("D:\\codefile\\python_code\\E2\\words.txt")
    #将单词存入字典
    for line in file:
        word = line.strip()
        if 'i' in word or 'a' in word:
            words_dic[len(word)].add(word)
    file.close()
    words_dic[1] = {'i', 'a'}


def find_cutable():
    global words_dic, maxlen, word_list
    for i in range(maxlen, 1, -1):
        for word in words_dic[i]:
            cut(word)
            if flag:
                return
            word_list.clear()


def cut(need_cut_word):
    global words_dic
    global flag
    global word_list
    word_list.append(need_cut_word)
    templen = len(need_cut_word)
    #print(templen)
    curlen = templen
    if curlen == 1:
        flag = True
        return 
    for j in range(templen):
        temp_word = need_cut_word[:j] + need_cut_word[j + 1:]
        if temp_word in words_dic[curlen - 1]:
            cut(temp_word)
    if flag:
            return
    word_list.pop()



def main():
    read_file()
    find_cutable()
    for i in range(len(word_list), 0, -1):
        if len(word_list[-1]) != 1:
            word_list.pop()
    for i in word_list:
        print(i)


if __name__ == '__main__':
    tt = time.time()
    words_dic = {}
    word_list = []
    maxlen = 0
    minlen = 0
    flag = False
    main()

    print(time.time() - tt)





#file中，如果line已经用了一次，不可以重复使用，可能因为指针已经移到了文件最后

#字典推导式，实现进行键的循环，还是先进行值得循环
