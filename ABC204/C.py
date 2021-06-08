import sys
sys.setrecursionlimit(10000)
 
n, m = map(int, input().split())
 
x = [[] for i in range(n)]
 
def dfs(i):
  if done[i]==True:
    return
  else:
    done[i]=True
    for next in x[i]:
      dfs(next)
 
for i in range(m):
  a, b = map(int, input().split())
  x[a-1].append(b-1)
 
ans = 0  
for s in range(n):
  done = [False]*n
  dfs(s)
  ans += sum(done)
 
print(ans)