def main():
    N = int(input())
    A_list, P_list, X_list = [], [], []
    P_min = 10 ** 10

    for _ in range(N):
        A, P, X = map(int, input().split())
        A_list.append(A), P_list.append(P), X_list.append(X)
    
    for i in range(N):
        if X_list[i] - A_list[i] >= 1:
            P_min = min(P_min, P_list[i])

    print(-1) if P_min == 10 ** 10 else print(P_min)


if __name__ == "__main__":
    main()