from sys import stdin

input = stdin.readline
N = int(input())
A = list(map(int, input().split()))
count = -1
flag = True

while flag:
    for i in range(N):
        if A[i] % 2 == 1:
            flag = False
            break

    count += 1
    A = list(map(lambda n: n / 2, A))

print(count)


# --------再帰関数を使う場合-------- #
# def shift_only(A, N):
#     global count
#     for i in range(N):
#         if A[i] % 2 == 1:
#             return count
    
#     count += 1
#     shift_only(list(map(lambda n: n / 2, A)), N)
#     return count

# print(shift_only(A, N))