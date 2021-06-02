def main():
    S = input()

    for i in range(len(S)):
        if i % 2 == 0 and not S[i].islower():
            print("No")
            exit()
        elif i % 2 != 0 and S[i].islower():
            print("No")
            exit()
    
    print("Yes")


if __name__ == "__main__":
    main()