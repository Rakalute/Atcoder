def main():
    H, W, X, Y = map(int, input().split())
    map_list = [] # 各マスの障害物の有無を記録したリスト
    ans = 0
    
    for _ in range(H):
        map_list.append(list(input()))
    
    for y in range(Y - 1)[::-1]:
        if map_list[X - 1][y] == ".": 
            ans += 1
        else:
            break

    for y in range(Y, W):
        if map_list[X - 1][y] == ".":
            ans += 1
        else:
            break
    
    for x in range(X - 1)[::-1]:
        if map_list[x][Y - 1] == ".":
            ans += 1
        else:
            break
    
    for x in range(X, H):
        if map_list[x][Y - 1] == ".":
            ans += 1
        else:
            break
    
    print(ans + 1)


if __name__ == "__main__":
    main()