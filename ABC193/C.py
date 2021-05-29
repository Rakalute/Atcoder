def main():
    N = int(input())
    ab_set = set()

    # b>=2よりaは最大でもlog(N)
    # a>=2よろbは最大でも33になる(2 ** 33 = 8589934592)
    for a in range(2, 10 ** 5 + 1):
        for b in range(2, 34):
            if N >= a ** b:
                ab_set.add(a ** b)
            if a ** b > N: break

    print(N - len(ab_set))


if __name__ == "__main__":
    main()


# for a in range(2, a_max):
#     b = math.log(N, a) # logの計算をすると答えがfloat型になる
#     if not b.is_integer:
#         pair_num += 1