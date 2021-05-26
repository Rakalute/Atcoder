from sys import stdin

input = stdin.readline
S = input()
o_num = 0
o_index = [] # 文字列Sで"o"が含まれる添え字番号のリスト


# 整数sが暗証番号の条件を満たしているか確認
def judge(s):
    # 暗証番号の各桁が高橋の記憶に含まれている可能性があるか確認
    # 更に，oの数字が使用されているかをチェックする
    if S[int(s[0])] != "x" and S[int(s[1])] != "x" and S[int(s[2])] != "x" and S[int(s[3])] != "x":
        for j in range(o_num):
            if str(o_index[j]) not in s: return False
        return True


def main():
    global o_num, o_index
    count = 0
    
    # oが4つ以下かをチェック
    # Sでのoの添え字番号をリストとして保存
    for index, mk in enumerate(S):
        if mk == "o": 
            o_num += 1
            o_index.append(index)
        if o_num >= 5:
            print(0)
            exit()

    for i in range(10000):
        s = str(i).zfill(4) # "0000"~"9999"を生成可能
        if judge(s): count += 1
    
    print(count)


if __name__ == "__main__":
    main()