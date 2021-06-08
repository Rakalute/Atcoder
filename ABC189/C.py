def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0

    for i in range(N):
        minimum = A[i]
        for j in range(i, N):
            minimum = min(minimum, A[j])
            ans = max(ans, minimum * (j - i + 1))

    print(ans)
            
   
if __name__ == "__main__":
       main()