def main():
    # 長さ2Nの文字列S
    N = int(input())
    S = list(input())

    # queryの数
    Q = int(input())

    flag = False

    # queryの数だけfor文を回す
    for _ in range(Q):
        T, A, B = map(int, input().split())

        if T == 1 and flag == False:
            S[A - 1], S[B -1] = S[B - 1], S[A - 1]
        elif T == 1 and flag == True:
            if A <= N and B > N:
                S[A + N - 1], S[B - N - 1] = S[B - N - 1], S[A + N - 1]
            elif A <= N and B <= N:
                S[A + N - 1], S[B + N - 1] = S[B + N - 1], S[A + N - 1]
            elif A> N and B > N:
                S[A - N - 1], S[B - N - 1] = S[B - N - 1], S[A - N - 1]
        elif T == 2:
            flag = False if flag else True
        else:
            pass
    
    if flag:
        S_front, S_back = S[:N], S[N:]
        S = S_back + S_front

    print("".join(S))


if __name__ == "__main__":
    main()