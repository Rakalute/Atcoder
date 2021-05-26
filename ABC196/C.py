def main():
    N = input()

    # 0~9の場合0を出力し，プログラム終了
    if int(N) < 9:
        print(0)
        exit()

    if len(N) % 2 == 1:
        N = str(int(N) - (int(N[1:]) + 1))

    N_half = len(N) // 2
    N_front = int(N[-2*N_half: -N_half])
    N_back = int(N[-N_half:])

    print(N_front - 1) if N_front > N_back else print(N_front)


# def main2():
#     N = int(input())
#     ans = 0

#     for i in range(1, 1000001):
#         if int(str(i) * 2) <= N:
#             ans += 1
#         else:
#             print(ans)
#             exit()



if __name__ == "__main__":
    main()
