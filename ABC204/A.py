xy = list(map(int, input().split()))

if xy[0] == xy[1]:
    print(xy[0])
elif not 1 in xy:
    print(1)
elif not 2 in xy:
    print(2)
elif not 0 in xy:
    print(0)
