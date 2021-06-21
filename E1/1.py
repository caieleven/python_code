define calculate1():
    x = 0
    for i in range(0, 9):
        x = x * 100 + 15
    y = 0
    for i in range(0, 19):
        y = y * 10 + 3;
    result = x * y
    print("result is:")
    print(result)
    temp_result = result
    sum = 0;
    while temp_result != 0:
        sum += temp_result%10
        temp_result = int(temp_result / 10)
    print("the sum of these numbers is:")
    print(sum)
    return


define calculate2():
    ans = 1
    for i in range(0,2015):
        ans *= 2016
    return

calculare1()




