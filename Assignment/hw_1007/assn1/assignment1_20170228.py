import time

def iterfibo(n):
    fibo = [0,1]

    for i in range(2, n+1):
        fibo.append(fibo[i-1]+fibo[i-2])

    return fibo[-1]

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("iterfibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
