## 効率の良いアルゴリズム
# def main():
#     N = int(input())
#     A_time, B_time = [], []
    
#     for _ in range(N):
#         A, B = map(int, input().split())
#         A_time.append(A), B_time.append(B)

#     A_minIdx = A_time.index(min(A_time))
#     B_minIdx = B_time.index(min(B_time))

#     A_time.sort(), B_time.sort()
#     A_min, B_min = min(A_time), min(B_time)

#     if A_minIdx == B_minIdx:
#         if A_min + B_min <= min(A_time[1], B_time[1]):
#             print(A_min + B_min)
#         elif A_min + B_min > min(A_time[1], B_time[1]):
#             print(max(min(A_time[1], B_time[1]), A_min, B_min))
#     else:
#         print(max(A_min, B_min))

    
# 全探索(O(N**2))
def main():
    N = int(input())
    A_time, B_time = [], []
    ans = 10 ** 6

    for _ in range(N):
        A, B = map(int, input().split())
        A_time.append(A), B_time.append(B)

    for a in range(N):
        for b in range(N):
            if a == b:
                total = A_time[a] + B_time[b]
            else:
                total = max(A_time[a], B_time[b])
            ans = min(ans, total)
    
    print(ans)


if __name__ == "__main__":
    main()