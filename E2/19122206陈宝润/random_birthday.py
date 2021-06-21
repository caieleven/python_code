import random


def main():
    m = int(input("M: "))
    n = int(input("N: "))
    birthday = {i:{random.randint(0, 365) for j in range(n)} for i in range(m)}
    num = 0
    for i in birthday.keys():
        if len(birthday[i]) < n:
            num += 1
    print(num / m)

if __name__ == '__main__':
    main()

    