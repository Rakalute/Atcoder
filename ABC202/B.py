def main():
    # 文字列を反転
    S = list(input()[::-1])

    for i in range(len(S)):
        if S[i] == "6":
            S[i] = "9"
        elif S[i] == "9":
            S[i] = "6"
        else:
            pass

    print("".join(map(str, S)))

if __name__ == "__main__":
    main()