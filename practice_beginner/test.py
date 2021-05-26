# a = [i * 2 for i in range(4)]
# print(a)

# a, b, c, x = [int(input()) for i in range(4)]
# a, b, c, x = map(int, [input() for i in range(4)])

# print(a, b, c, x)

# a, b = map(int, input().split())
# print(a, b)

# a = 125
# print(list(str(a)))

# square = 0
# max_num = 10 ** 18

# while True:
#     if max_num >= 2 ** square:
#         square += 1
#     else:
#         print(square)
#         break

# from collections import deque

# test_list = [1, 2, 3, 4]
# test_list2 = [1, 2, 3]
# test_list = deque(test_list)

# print(test_list)
# print(test_list2)

# a = [2, 3, 4, 2, 1, 1]
# b = list(set(a))
# print(b)

# a = [1, 2, 3]
# print(a[-3:])

# t_next, x_next, y_next = map(int, input().split())
# print(t_next, x_next, y_next)


# test_list = [["a", 1], ["s", 3], ["b", 2]]
# test_list.sort()
# print(test_list[1][0])

N = 3

a = N if N == 3 else print("error")

print(a)