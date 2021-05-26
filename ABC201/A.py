from sys import stdin

def main():
    A = sorted(list(map(int, input().split())))
    print("Yes") if A[2] - A[1] == A[1] - A[0] else print("No")

if __name__ == "__main__":
    main()


# test_dict = {"a": 1, "b": 2}
# list(test_dict)
# print(test_dict[0][0])
