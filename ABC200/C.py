from sys import stdin

# 200で割った余りが等しいものは条件を満たすと考える
def main():
    input = stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    mod_list = [0] * 200
    count = 0 # 条件を満たす整数の個数

    # 配列Aを200で割った余りの分布を求める
    for i in range(N): mod_list[A[i] % 200] += 1

    for i in range(200):
        num = mod_list[i]
        if num > 1:
            count += num * (num -1) // 2

    print(count)

if __name__ == "__main__":
    main()



# for i in range(N):
#     for j in range(i + 1, N):
#         if (A[i] - A[j]) % 200 == 0: count += 1 