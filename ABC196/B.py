def main():
    X = list(input())
    A = []

    for i in X:
        if i == ".": break
        A.append(i)
    
    print("".join(A))

if __name__ == "__main__":
    main()