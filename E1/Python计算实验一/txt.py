words = []  # 全局变量
frequency = {}


def read_file():  # 读取文件
    global words
    file = open("D:\\codefile\\python_code\\E2\\words.txt")
    for line in file:
        words.append(line.strip())
    file.close()


def calculate_frequency():
    global frequency
    global words
    words_set = set(words)
    for word in words_set:
        frequency[word] = words.count(word)


def main():
    read_file()
    calculate_frequency()
    output_the_rate()


def output_the_rate():
    global words
    global frequency
    file = open("newword.txt")
    newwords = []
    num = len(words)
    for line in file:
        newwords.append(line.strip())
    file.close()
    for newword in newwords:
        if newword in frequency.keys():
            print(newword, '的频率是', frequency[newword] / num)
        else:
            print(newword, '没有出现过')


if __name__ == '__main__':
    main()
