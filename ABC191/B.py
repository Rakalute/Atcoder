def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    index = 0

    for _ in range(N):
        if A[index] == X:
            del A[index]
        else:
            index += 1
            

    print(" ".join(list(map(str, A))))


if __name__ == "__main__":
    main()