def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = [None] * N
    E = [0] * N
    count = 0

    # B[C[j]]の値をD[j]に格納
    for j in range(N):
        D[j] = B[C[j] - 1] - 1

    # Dの値の分布を求める
    for i in range(N):
        E[D[i]] += 1
    
    for i in range(N):
        count += E[A[i] - 1]




    # for i in range(N):
    #     for j in range(N):
    #         if C[j] < N and A[i] == B[C[j]]:
    #             count += 1
    
    print(count)



if __name__ == "__main__":
    main()
