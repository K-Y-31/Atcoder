#1

a, b = map(int, input().split())
c, d = map(int, input().split())
res = -200
for i in range(a, b+1):
    for j in range(c, d+1):
        ans = i-j
        res = max(res, ans)
print(res)

#2
x = input()
print(x.split('.')[0])

#3

n = int(input())
for i in range(1, 1000001):
    if int(str(i)*2) > n:
        print(i-1)
        exit()

#4
h, w, a, b = map(int, input().split())
ans = 0

def dfs(i, bit, a, b):
    if i == h*w:
        global ans
        ans += 1
        return
    if bit >> i & 1:
        dfs(i+1, bit, a, b)
        return
    if b:
        dfs(i+1, bit | 1 << i, a, b-1)
    if a:
        if i % w != w-1 and not bit & 1 << (i+1):
            dfs(i+1, bit | 1 << i | 1 << (i+1), a-1, b)
        if i + w < h*w:
            dfs(i+1, bit | 1 << i | 1 << (i+w), a-1, b)
dfs(0, 0, a, b)
print(ans)
