import itertools

def main():
    N, M = map(int, input().split())
    cond = [None] * M

    for i in range(M):
        cond[i] = set(map(int, input().split()))
    
    K = int(input())
    put = [None] * K
    ans = 0

    for i in range(K):
        put[i] = list(map(int, input().split()))

    # アンパック(*)を使うことで多次元配列を引数にすることが可能(直積)
    direct = list(map(set, itertools.product(*put)))

    direct_len = len(direct)

    for i in range(direct_len):
        count = 0
        for j in range(M):
            if cond[j] & direct[i] == cond[j]:
                count += 1
        ans = max(ans, count)
    
    print(ans)
    

if __name__ == "__main__":
    main()