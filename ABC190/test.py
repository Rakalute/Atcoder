import itertools

# a = [1, 4]
# b = [1, 3]
# c = [2, 5]

# A = [[1, 4], [1, 3], [2, 5]]

# print(list(itertools.product(*A)))

# cond = [[1, 4], [1, 3], [2, 5]]
# put = [[2, 3], [1, 3], [5, 3]]
# A = set(cond) & set(put)

# if A != set():
#     print("Yes")
# else:
#     print("No")

# cond = [None] * 4

# for i in range(4):
#     cond[i] = set(map(int, input().split()))

# print(cond)

put = [[1, 2], [1, 4], [5, 6]]

direct = list(map(set, itertools.product(*put)))

print(direct)