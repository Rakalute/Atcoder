# from sys import stdin
# from collections import deque

# input = stdin.readline

# N = int(input())
# Card = list(map(int, input().split()))
# Card.sort()

# Card = deque(Card) # Cardをdequeに変換する
# alice_point = 0
# bob_point = 0


# # while (Card == []):
# # 上記の書き方はdequeに適応できない 
# while (Card != deque([])):
#     alice_point += Card.pop()
#     if Card != deque([]): bob_point += Card.pop()


# print(alice_point - bob_point)


# 模範解答
from sys import stdin
from collections import deque

input = stdin.readline
N = int(input())
Card = sorted(list(map(int, input().split())))

print(sum(Card[(N - 1)::-2]) - sum(Card[(N - 2)::-2]))
