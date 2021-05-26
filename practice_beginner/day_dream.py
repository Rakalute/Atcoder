"""
空文字列Tの末尾に4つのいづれかの単語を追加する処理を繰り返し
文字列Sと同じにすることができるか判定せよ.
文字列Sを空にすることができるかどうかで判定する．
"""

from sys import stdin

input = stdin.readline().rstrip
S = input()

for _ in range(20000):
    if not S:
        print("YES")
        break
    elif S[-5:] == "dream":
        S = S[:-5]
    elif S[-7:] == "dreamer":
        S = S[:-7]
    elif S[-5:] == "erase":
        S = S[:-5]
    elif S[-6:] == "eraser":
        S = S[:-6]
    else:
        print("NO")
        break


# for _ in range(20000):
#     if not S:
#         print("YES")
#         break
#     elif S[-5:] == "dream":
#         if S == "dream":
#             S = ""
#         else:
#             S = S[:-5]
#     elif S[-7:] == "dreamer":
#         if S == "dreamer":
#             S = ""
#         else:
#             S = S[:-7]
#     elif S[-5:] == "erase":
#         if S == "erase":
#             S = ""
#         else:
#             S = S[:-5]
#     elif S[-6:] == "eraser":
#         if S == "eraser":
#             S = ""
#         else:
#             S = S[:-6]
#     else:
#         print("NO")
#         break