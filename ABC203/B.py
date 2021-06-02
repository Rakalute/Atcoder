def main():
    N, K = map(int, input().split())
    room = 0
    total = 0


    for n in range(1, N + 1):
        for k in range(1, K + 1):
            room = int(str(n) + "0" + str(k))
            total += room
    
    print(total)


if __name__ == "__main__":
    main()
