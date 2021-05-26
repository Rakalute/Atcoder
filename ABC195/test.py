def main():
    M, H = map(int, input().split())
    print("Yes") if H % M == 0 else print("No")

if __name__ == "__main__":
    main()