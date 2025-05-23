import sys
input = sys.stdin.readline

n = int(input())
s, w = [0]*n, [0]*n

def solve(i, cnt):
    global ans
    if i == n:
        ans = max(ans, cnt)
        return
    if s[i] <= 0:
        solve(i+1, cnt)
    else:
        flag = False
        for cur in (n):
            if i == cur or s[cur] <= 0:
                continue
            flag = True
            s[i] -= w[cur]
            s[cur] -= w[i]
            solve(i+1, cnt+int(s[i]<=0)+int(s[cur]<=0))
            s[i] += w[cur]
            s[cur] += w[i]
        if flag == False:
            solve(i+1, cnt)
            
for i in range(n):
    s[i], w[i] = map(int, input().split())

ans = 0
solve(0, 0)
print(ans)