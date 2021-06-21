import math
import time
if __name__ == "__main__":
        x = 0
        k = 1
        temp = 1103
        tt = time.time()
        while True:
                if math.pi - x <= 1.0e-30:
                        print("caculator: \t", x)
                        print("math.pi:   \t", math.pi)
                        break
                else:
                        temp += math.factorial(4*k)*(1103 + 26390*k) / (math.pow(math.factorial(k), 4) * math.pow(396, 4*k))
                        x = 9801 / (2 * math.pow(2, 0.5) * temp)
                        k +=1
        print(time.time() - tt)
