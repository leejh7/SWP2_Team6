# 20160176 송영진
import sys
line = int(input("line: "))
tri = 1
for i in range(line):
    for j in range(tri):
        print('*', end='')
    if(tri == line):
        break
    tri += 1
    print()

# 20181675 이준호
n = int(input("\nEnter a number: "))
print("\n".join(('*' * i for i in range(1, n+1))))

# 20185290 이하영
print("Enter a number:")
n = int(input())
for i in range(1, n+1):
    print("*"*i)

# 20190406 이현지
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print("*"*i)

# 20191670 조나영

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    print("*" * i)

# 20170228 한윤서
n = int(input("n:"))

for i in range(1, n+1):
    print('*'*i)
