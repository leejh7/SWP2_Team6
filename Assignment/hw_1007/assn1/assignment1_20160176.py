import time

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def iterFibo(n):
    if n <= 2:
        return 1

    curr, next = 0, 1
    for i in range(n):
        curr, next = next, curr + next
    return curr

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fib(nbr)
    ts = time.time() - ts
    print("fib(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = iterFibo(nbr)
    ts = time.time() - ts
    print("iterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
