## 全探索(時間オーバー)
# def main():
#     N = int(input())
#     A = list(map(int, input().split()))
#     ans = 0

#     for i in range(N - 1):
#         for j in range(i + 1, N):
#             ans += (A[i] - A[j]) ** 2
    
#     print(ans)

# 効率の良いアルゴリズム
def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_elm = [0] * 401 # -200 ~ 200
    ans = 0

    for i in range(N):
        if A[i] >= 0:
            A_elm[(A[i] + 200)] += 1
        else:
            A_elm[200 - abs(A[i])] += 1
    
    for i in range(400):
        for j in range(i + 1, 401):
            i_conv, j_conv = i - 200, j - 200
            ans += ((i_conv - j_conv) ** 2) * (A_elm[i] * A_elm[j])

    print(ans)


if __name__ == "__main__":
    main()