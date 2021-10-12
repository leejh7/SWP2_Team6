import time
import random

def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1


def recbinsearch(array,start,end,target):
    if start>end :
        return None
    mid = (start+end) // 2
    if array[mid] == target :
        return mid
    elif array[mid] > target :
        return recbinsearch(array,start,mid-1, target)
    else:
        return recbinsearch(array,mid+1,end,target)




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

# binary search
cnt = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers),target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("Binary Search %d: not found %d time %.6f" % (numoftargets, cnt, ts))

ts = time.time()

# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("Sequential Search %d: not found %d time %.6f" % (numoftargets, cnt, ts))
