def main():
    N , K = map(int, input().split())
    F = []
    total = K


    for _ in range(N):
        # 村AでB円渡す
        A, B = map(int, input().split())
        F.append([A, B])

    # 村番号でソートする
    F = sorted(F, key=lambda x: x[0])

    for i in range(len(F)):
        # 所持金が村番号より小さかったらそれ以上先にいけない
        if total < F[i][0]:
            print(total)
            exit()
        else:
            total += F[i][1]

    print(total)


if __name__ == "__main__":
    main()





    # for _ in range(N - 1):
    #     if F[count][0] == F[count + 1][0]:
    #         F[count][1] += F[count + 1][1]
    #         del F[count + 1]
    #     else:
    #         count += 1
