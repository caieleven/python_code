def Ack(m, n):
    if not isinstance(m, int) or not isinstance(n, int) or m < 0:
        return 0
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return Ack(m-1, 1)
    else:
        return Ack(m - 1, Ack(m, n-1))

print(Ack(3, 1))
