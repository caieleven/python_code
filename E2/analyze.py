import matplotlib.pyplot as plt
import random
def genelist(nlist):
    m = 5000
    plist=[]
    for n in nlist:
        birthday = {i:{random.randint(0, 365) for j in range(n)} for i in range(m)}
        num = 0
        for i in birthday.keys():
            if len(birthday[i]) < n:
                num += 1
        plist.append(num/m)
        birthday.clear()
    return plist




def main():
    nlist = [10, 20, 30, 40, 50, 100, 200, 300, 366]
    plist = genelist(nlist)
    plt.plot(nlist, plist)
    plt.xlabel("Class Size:N")
    plt.ylabel("Probability:P")
    plt.show()


if __name__ == "__main__":
    main()