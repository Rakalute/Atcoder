def main():
    N, S, D = map(int, input().split())
    magic = [None] * N

    for i in range(N):
        mag = list(map(int, input().split()))
        magic[i] = mag
    
    for i in range(N):
        if magic[i][0] < S and magic[i][1] > D:
            print("Yes")
            exit()
    
    print("No")


if __name__ == "__main__":
    main()