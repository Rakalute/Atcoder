"""
お札N枚でY円があり得るか判定し，あり得る場合は例を1つ示せ
お札は10000円，5000円，1000円のみを指す
"""

from sys import flags, stdin

input = stdin.readline
N, Y = map(int, input().split())
flag = 0


for x in range(N + 1):
    for y in range(N + 1 - x):
        z = N - (x + y)
        if 10000 * x + 5000 * y + 1000 * z == Y:
            print(x, y , z)
            exit()

print(-1, -1, -1)





# x_num = Y // 10000

# if x_num == 0:
#     pass
# else:
#     for x in range(x_num):


# for i in range(2000):
#     x = i
#     y = (Y - 10000 * x) // 5000
#     z1 = Y - (10000 * x + 5000 * y)
#     z2 = (Y - 10000 * x) // 1000

#     if x + y + z1 == N:
#         flag = 1
#         break
#     if x + y + z2 == N:
#         flag = 2
#         break

# if flag == 1:
#     print(x, y, z1)
# elif flag == 2:
#     print(x, y, z2)
# else:
#     print(-1, -1, -1)