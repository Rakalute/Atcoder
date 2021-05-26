def main():
    S = list(input())
    S_topPop = S.pop(0)
    # joinで文字列のリストを連結
    print("".join(S) + S_topPop)

if __name__ == "__main__":
    main()