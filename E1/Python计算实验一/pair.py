import time
words = []#全局变量
frequency = []
def read_file():#读取文件
    global words
    ans = 0
    file = open("D:\\codefile\\python_code\\E1\\Python计算实验一\\words.txt")
    for line in file:
        words.append(line.strip())
        frequency[len(words[ans])] += 1
        ans += 1
    print(len(words))


def sort_key(elem):#排序所使用的排序关键词
    return len(elem)

def initialize_frequency():#初始化频数
    global frequency
    for i in range(22):
        frequency.append(0)

def calculate_range():#计算相同长度单词所在范围
    #frequency[i]表示长度为i的最后一个单词的索引
    global frequency
    for i in range(21):
        frequency[i + 1] += frequency[i]

def find_reverse():#查找并输出反序对
    global words
    global frequency
    num  = 0
    for i in range(2,22):
        range_len = frequency[i] - frequency[i - 1]
        start = frequency[i - 1]
        for j in range(range_len):
            #for k in range(range_len):
            if words[start][::-1] in words[start : frequency[i]]:
                print(words[start],words[start][::-1])
                num += 1
            start += 1
    print(num)

def main():
    t = time.time()
    initialize_frequency()
    read_file()
    words.sort(key = sort_key)
    calculate_range()
    find_reverse()
    print(time.time() - t)


if __name__ == '__main__':
    main()


