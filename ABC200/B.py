from sys import stdin

input = stdin.readline


def main():
    N, K = map(int, input().split())

    for _ in range(K):
        # str型になったNをint型に変換する
        N = int(N)
        N = N / 200 if N % 200 == 0 else str(N) + "200"

    print(int(N))

if __name__ == "__main__":
    main()
