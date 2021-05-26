# from sys import stdin

# input = stdin.readline

# N, A, B = map(int, input().split())
# N_allTotal = 0 # 条件を満たす各桁の和の合計

# for N_int in range(1, N + 1):

#     N_str = str(N_int)
#     N_len = len(N_str)
#     N_total = 0 # 各桁の和

#     for i in range(N_len)[::-1]:
#         N_total += int(N_str[i])
    
#     if N_total >= A and N_total <= B:
#         N_allTotal += N_int


# print(N_allTotal)


from sys import stdin

input = stdin.readline

N, A, B = map(int, input().split())
N_Total = 0 # 条件を満たす整数の合計

for i in range(1, N + 1):
    if A <= sum(list(map(int, list(str(i))))) <= B: N_Total += i

print(N_Total)
