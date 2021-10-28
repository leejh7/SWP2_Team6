import time
import random

def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1

def recbinsearch(array, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return recbinsearch(array, target, start, mid - 1)
    else:
        return recbinsearch(array, target, mid + 1, end)

numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]

ts = time.time()

# binary search - recursive
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, target, 0, len(numbers))
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
