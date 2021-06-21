from time import time
import cv2

num = 0
loc_x = []
loc_y = []

def Get_Loc_Cha(x, y):
        global loc_x
        global loc_y
        global num
        t=0
        for i in range(int(len(x)/2)):
                if x[i][0]==chr(t+97):
                        loc_x.append(i)
                        t+=1
                        if t==26:
                                break
        num = t
        t = 0
        for i in range(len(x)):
                if y[i][0]==chr(t+97):
                        loc_y.append(i)
                        t+=1
                if y[i][0]==chr(t+97+1):
                        loc_y.append(-1)
                        loc_y.append(i)
                        t+=2
                if t>25:
                        break
        loc_x.append(int(len(x)/2))
        loc_y.append(len(x))

def Find_reverse(tx,ty):
        frex = []
        frey = []
        for i in range(22):
                frex.append(0)
                frey.append(0)
        
        for i in range(len(tx)):
                frex[len(tx[i])] += 1
        for i in range(len(ty)):
                frey[len(ty[i])] += 1
        
        tx.sort(key = sort_key)
        ty.sort(key = sort_key)

        for i in range(21):
                frex[i + 1] += frex[i]
                frey[i + 1] += frey[i]

        for i in range(2,22):
                range_len_x = frex[i] - frex[i-1]
                start_x = frex[i - 1]
                for j in range(range_len_x):
                        if tx[start_x + j] in ty[frey[i-1] : frey[i]]:
                                print(tx[start_x + j], " & ", tx[start_x + j][::-1])
                        

def sort_key(e):
        return len(e)

def main():
        tt=time()

        word = open('words.txt', 'r')
        x = word.read().split()
        word.close()
        y=list(map(lambda s: s[::-1],x))
        y.sort()
        
        Get_Loc_Cha(x, y)
        
        for i in range(num):
                if loc_y[i]==-1:
                        i+=1
                tx = x[loc_x[i]:loc_x[i+1]]
                ty = y[loc_y[i]:loc_y[i+1]]
                Find_reverse(tx,ty)
                
        print(time()-tt)


if __name__== "__main__":
        main()
