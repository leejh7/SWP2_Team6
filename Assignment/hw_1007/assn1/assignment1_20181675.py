import time
import random


def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


def Iter_fibo(n):
    memo = [0 for i in range(n+1)]
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    iter_ts = time.time()
    iter_fibonumber = Iter_fibo(nbr)
    iter_ts = time.time() - iter_ts
    print("IterFibo(%d)=%d, time %.6f" % (nbr, iter_fibonumber, iter_ts))
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
