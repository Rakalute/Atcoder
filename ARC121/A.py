def main():
    N = int(input())
    X = []
    Y = []
    ans = 0
    # Z = []

    for i in range(N):
        x, y = map(int, input().split())
        X.append([x, i]), Y.append([y, i])
    
    X_sort = sorted(X, reverse = True, key=lambda x: x[0])
    Y_sort = sorted(Y, reverse = True, key=lambda x: x[0])
    X_max, X_max2, X_min, X_min2 = X_sort[0], X_sort[1], X_sort[-1], X_sort[-2]
    Y_max, Y_max2, Y_min, Y_min2 = Y_sort[0], Y_sort[1], Y_sort[-1], Y_sort[-2]


    # Xが最大値
    if (X_max[0] - X_min[0]) >= (Y_max[0] - Y_min[0]) and X_max[1] != Y_max[1] and X_min[1] != Y_min[1]:
        ans = max(X_max[0] - X_min2[0], X_max2[0] - X_min[0], Y_max[0] - Y_min[0])
        print(ans)
    elif (X_max[0] - X_min[0]) >= (Y_max[0] - Y_min[0]) and X_max[1] == Y_max[1] and X_min[1] != Y_min[1]:
        ans = max(X_max[0] - X_min2[0], X_max2[0] - X_min[0], Y_max2[0] - Y_min[0])
        print(ans)
    elif (X_max[0] - X_min[0]) >= (Y_max[0] - Y_min[0]) and X_max[1] != Y_max[1] and X_min[1] == Y_min[1]:
        ans = max(X_max[0] - X_min2[0], X_max2[0] - X_min[0], Y_max[0] - Y_min2[0])
        print(ans)
    elif (X_max[0] - X_min[0]) >= (Y_max[0] - Y_min[0]) and X_max[1] == Y_max[1] and X_min[1] == Y_min[1]:
        ans = max(X_max[0] - X_min2[0], X_max2[0] - X_min[0], Y_max2[0] - Y_min2[0])
        print(ans)
    # Yが最大値
    elif (X_max[0] - X_min[0]) < (Y_max[0] - Y_min[0]) and Y_max[1] != X_max[1] and Y_min[1] != X_min[1]:
        ans = max(Y_max[0] - Y_min2[0], Y_max2[0] - Y_min[0], X_max[0] - X_min[0])
        print(ans)
    elif (X_max[0] - X_min[0]) < (Y_max[0] - Y_min[0]) and Y_max[1] == X_max[1] and Y_min[1] != X_min[1]:
        ans = max(Y_max[0] - Y_min2[0], Y_max2[0] - Y_min[0], X_max2[0] - X_min[0])
        print(ans)
    elif (X_max[0] - X_min[0]) < (Y_max[0] - Y_min[0]) and Y_max[1] != X_max[1] and Y_min[1] == X_min[1]:
        ans = max(Y_max[0] - Y_min2[0], Y_max2[0] - Y_min[0], X_max[0] - X_min2[0])
        print(ans)
    elif (X_max[0] - X_min[0]) < (Y_max[0] - Y_min[0]) and Y_max[1] == X_max[1] and Y_min[1] == X_min[1]:
        ans = max(Y_max[0] - Y_min2[0], Y_max2[0] - Y_min[0], X_max2[0] - X_min2[0])
        print(ans)

    

    # for i in range(N - 1):
    #     for j in range(i + 1, N):
    #         z = max(abs(X[i] - X[j]), abs(Y[i] - Y[j]))
    #         Z.append(z)

    # Z = sorted(Z, reverse = True)
    # print(Z[1])


if __name__ == "__main__":
    main()