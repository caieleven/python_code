from time import time

def main():
        tt=time()
        z = []
        file = open("words.txt")
        for line in file:
                t = line.strip()
                z.append(t)
                z.append(t[::-1])
        
        z.sort()

        for i in range(int(len(z)-1)):
                if z[i] ==z[i+1]:
                        print(z[i], "&", z[i][::-1])
                        i+=1
        
        print(time()-tt)

        while True:
                if (time()-tt) == 100:
                        break        

        
if __name__== "__main__":
        main()
