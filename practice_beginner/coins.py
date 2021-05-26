from sys import stdin

input = stdin.readline
A = int(input())
B = int(input())
C = int(input())
X = int(input())
total = 0
count = 0

for a in range(A + 1):
    for b in range(B + 1):
        for c in range(C + 1):
            total = (50 * c) + (100 * b) + (500 * a)
            if total == X: count += 1

print(count)

