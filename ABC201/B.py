from sys import stdin

def main():
    input = stdin.readline
    N = int(input())
    ST_list = []

    for _ in range(N):
        S, T = input().split()
        T = int(T)
        ST_list.append([T, S])

    ST_list.sort(reverse = True)
    print(ST_list[1][1])

if __name__ == "__main__":
    main()