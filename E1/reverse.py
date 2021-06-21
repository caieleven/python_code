from time import time

def main():
        t=time()
        print(t)
        word = open('words.txt', 'r')
        x = word.read().split()
        word.close()
        
        y=list(map(lambda s: s[::-1],x))
        
        l=len(x)
        for i in range(int(l / 2)):
                for j in range(i + 1, l):
                        if x[i] == y[j]:
                                print(x[i], " & ", x[i][::-1])
                                break
        t=time()-t
        print(t)

if __name__== "__main__":
        main()
