"""
時刻0に点(0,0)を出発する．時刻tに点(x,y)に存在するとき時刻t+1には
(x+1,y), (x-1,y), (x,y+1), (x,y-1)のうちいづれかに必ず存在する．
"""

from sys import stdin

def main():   
    input = stdin.readline
    N = int(input())
    t, x, y, = 0, 0, 0 # t=x=y=0とも書ける

    for _ in range(N):
        t_next, x_next, y_next = map(int, input().split())
        time_delta = t_next - t
        distance = abs(x_next - x) + abs(y_next - y)

        # distanceがtime_deltaより大きい場合
        if distance > time_delta:
            print("No")
            exit()

        # distanceがtime_deltaより小さいかつ，差が奇数の場合
        if (time_delta - distance) % 2 == 1:
            print("No")
            exit()
        
        # t, x, yを更新
        t, x, y = t_next, x_next, y_next

    print("Yes")


if __name__ == "__main__":
    main()