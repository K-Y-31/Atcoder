#1

r = int(input())
if r < 1200:
    print("ABC")
elif 1200 <= r < 2800:
    print('ARC')
elif 2800 <= r:
    print('AGC')

#2

a = input()
f_a = a[0]
count_c = 0
all_count = 0
for e in a[2:-1]:
    if e == "C":
        count_c += 1
for e in a:
    if e in 'abcdefghijklmnopqrstuvwxyz':
        all_count += 1
if f_a == "A" and count_c == 1 and all_count == len(a)-2:
    print('AC')
else:
    print('WA')
        

#3

d, g = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]
pc = pc[::-1]
ans = float('inf')
for i in range(d**2):
    total = 0
    cnt = 0
    for j in range(d):
        if 1&(i>>j):
            total += 100*(d-j)*pc[j][0]+pc[j][1]
            cnt += pc[j][0]
    if total >= g:
        ans = min(ans, cnt)
        continue
    for j in range(d):
        if not 1&(i>>j):
            for k in range(pc[j][0]):
                total += 100*(d-j)
                cnt += 1
                if total >= g:
                    ans = min(ans, cnt)
                    break
            break
print(ans)

#4

d = input()
n = len(d)
mod = 10**9+7

dp = [[0 for _ in range(4)] for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    if d[i] == "A":
        for j in range(4):
            dp[i+1][j] += dp[i][j]
        dp[i+1][1] += dp[i][0]
    elif d[i] == 'B':
        for j in range(4):
            dp[i+1][j] += dp[i][j]
        dp[i+1][2] += dp[i][1]
    elif d[i] == "C":
        for j in range(4):
            dp[i+1][j] += dp[i][j]
        dp[i+1][3] += dp[i][2]
    else:
        for j in range(4):
            dp[i+1][j] += dp[i][j]*3
        dp[i+1][1] += dp[i][0]
        dp[i+1][2] += dp[i][1]
        dp[i+1][3] += dp[i][2]
    for j in range(4):
        dp[i+1][j] %= mod
print(dp[n][3])

#5

n = int(input())
string = ""
while n != 0:
    r = n%2
    if r < 0:
        r += 2
    n = (n-r)//(-2)
    string += str(r)
string = string[::-1]
if string == "":
    string = "0"
print(string)

#6

from collections import defaultdict
n,m = map(int, input().split())
a = list(map(int, input().split()))
acc = [0]
ans = 0
for i in range(n):
    acc.append((acc[i]+a[i])%m)
amod = defaultdict(acc)
for e in acc:
    amod[e] += 1
for key, value in amod.items():
    ans += (value*(value-1)//2)
print(ans)
