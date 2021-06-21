import time
words = []
def read_file():
    global words
    ans = 0
    file = open("word.txt")
    for line in file:
        words.append(line.strip())
        words.append(line.strip()[::-1])

def find_reverse():
    

#def add_the_reversed():
#    global words
#    words_reversed = map(lambda x:x[::-1] words)
#    words += words_reversed

def main():
    read_file

if __name__ == '__main__':
    main()

