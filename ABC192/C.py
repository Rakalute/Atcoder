def main():
    N, K = input().split()
    N = list(map(int, list(N)))
    a = N

    for i in range(int(K)):
        g1 = int("".join(map(str, sorted(a, reverse = True))))
        g2 = int("".join(map(str, sorted(a))))
        a = list(map(int, list(str(g1 - g2))))
    
    print("".join(map(str, a)))


if __name__ == "__main__":
    main()

