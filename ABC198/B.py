def main():
    # 与えられるのは整数だが，文字列として扱う
    N = input()

    # Nのゼロ以外の整数部
    N_not = []
    flag = False

    for i in N[::-1]:
        if i != "0" or flag == True:
            flag = True
            N_not.append(i)
    
    # N_zeroの長さを2で割ったもの
    N_half = len(N_not) // 2

    if len(N_not) % 2 == 0:
        N_front = N_not[:N_half]
        N_back = N_not[N_half:][::-1]
    else:
        N_front = N_not[:N_half]
        N_back = N_not[N_half + 1:][::-1]

    print("Yes") if N_front == N_back else print("No")


# 他の回答
def main2():
    N = input()

    for i in range(10):
        N_pad = "0" * i + N
        if N_pad == N_pad[::-1]:
            print("Yes")
            exit()
    
    print("No")

if __name__ == "__main__":
    main()
    