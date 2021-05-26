import math

def main():
    R, X, Y = map(int, input().split())
    
    # 原点から(x, y)までのユークリッド距離
    R_xy = math.sqrt((X ** 2) + (Y ** 2))

    print(2) if R_xy < R else print(math.ceil(R_xy / R))
    
if __name__ == "__main__":
    main()


