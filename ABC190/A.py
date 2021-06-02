def main():
    A, B, C = map(int, input().split())

    if A > B:
        print("Takahashi")
    elif A == B:
        print("Aoki") if C == 0 else print("Takahashi")
    else:
        print("Aoki")

if __name__ == "__main__":
    main()