import math

def main():
    # みかんがAグラム以上Bグラム以下，重さがWキロになるように
    A, B, W = map(int, input().split())

    # Wをグラムに変換
    W = 1000 * W

    if W // A == W // B and (W % A != 0 and W % B != 0):
        print("UNSATISFIABLE")
    else:
        max_num = W // A
        min_num = math.ceil(W / B)
        print("{} {}".format(min_num, max_num))

if __name__ == "__main__":
    main()
