import math
def main():
    print("math.pi = ", math.pi)
    k = 0
    temppi = 0.0
    mypi = 0.0
    formula_1 = 9801 / pow(8, 0.5)
    formula_2 = 1103
    formula_3 = 1
    formula_3_p = pow(396, 4)
    temp_formula = 0.0
    while True:
        if mypi - temppi < 1.0e-15 and mypi != 0:
            print("my__.pi = ", "%.15f" % mypi)
            print(k)
            break
        else:
            temppi = mypi
            temp_formula += math.factorial(4 * k) * formula_2 / math.pow(math.factorial(k), 4) / formula_3
            mypi = 1 / temp_formula * formula_1
            formula_2 += 26390
            formula_3 *= formula_3_p
            k += 1


if __name__ == '__main__':
    main()
        


#格式化输出
#'%.7g'取三位有效数字
#'%.2e'取2位小数，用科学计数法
#round(a, 2)保留2位