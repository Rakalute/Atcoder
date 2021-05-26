from sys import stdin

def main():
    input = stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    fill_list = [] # Ai<=Biを満たす整数のリスト
    AB_andSet = [i for i in range(1, 1001)]
    # 全ての条件を満たす集合

    for i in range(N):
        if A[i] <= B[i]:
            for j in range(A[i], B[i] + 1):
                fill_list.append(j)
            
            # 2つの配列で共通する要素を求め，毎回更新
            AB_andSet = list(set(AB_andSet) & set(fill_list))
            fill_list = []

    print(len(AB_andSet))


if __name__ == "__main__":
    main()