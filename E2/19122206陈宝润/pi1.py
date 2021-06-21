if __name__ == "__main__":
    import math
    from time import time
    tt = time()
    val = math.pi
    print("math.pi = ", val)
    former = 2 * math.sqrt(2) / 9801
    sum = 0
    for k in range(0, 100):
        sum += math.factorial(4 * k) * (1103 + 26390 * k) / ((math.factorial(k) ** 4) * (396 ** (4 * k)))
    res = 1 / (former * sum)
    print("res = ", res)
    print(time()-tt)