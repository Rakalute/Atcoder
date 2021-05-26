# from sys import stdin

# input = stdin.readline

# N = int(input())
# d = sorted(map(int, [input() for i in range(N)]))
# # d = sorted(list(map(int, input().split())))

# answer = 1

# for i in range(N - 1):
#     if d[i] != d[i + 1]: answer += 1

# print(answer)

## 模範解答
from sys import stdin

input = stdin.readline
N = int(input())
print(len(set(map(int, [input() for i in range(N)]))))
