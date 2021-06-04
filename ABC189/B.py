def main():
    N, X = map(int, input().split())
    VP = [None] * N
    p_total = 0

    for i in range(N):
        VP[i] = list(map(int, input().split()))

    for n, vp_elm in enumerate(VP):
        V, P = vp_elm[0], vp_elm[1]
        p_total += V * P

        if p_total > X * 100:
            print(n + 1)
            exit()

    print(-1)

    # for i in range(1, N + 1):
    #     # 飲んだお酒の量Vml, アルコール度数P%
    #     V, P = map(int, input().split()) 
    #     p_total += V * (P / 100)

    #     if p_total > X:
    #         print(i)
    #         exit()


if __name__ == "__main__":
    main()