from time import time

def main():
        tt=time()
        file = open('words.txt', 'r')
        words = set(file.read().split())
        reverse = set()
        for word in words:
                if word[::-1] in words:
                        reverse.add(word)
        print(reverse)
        print(time() - tt)
                        
          
        
if __name__== "__main__":
        main()
