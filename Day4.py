#1

r,c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]

black = [0 for _ in range(c)]
for i in range(r):
    for j in range(c):
        black[j] += a[i][j]

res = 0
for i in range(c):
    res += max(black[i], r-black[i])

for i in range(2**r):
    black_diff = [o for _ in range(c)]
    for j in range(r):
        if i & (1 << j):
            for k in range(c):
                if a[j][k]:
                    black_diff[k] -= 1
                else:
                    black_diff[k] += 1
    sm = 0
    for j in range(c):
        sm += max(black[j]+black_diff[j], r-(black[j]+black_diff[j]))
    res = max(res, sm)
print(res)

#2

n, k = map(int, input().split())
a = list(map(int, input().split()))

res = float("inf")
for i in range(2**n):
    if (i%2==0):
        continue

    use_idx = [0 for _ in range(n)]
    use_cnt = 0
    for j in range(n):
        if i & (1 << j):
            use_idx[j] = 1
            use_cnt += 1

    if (use_cnt != k):
        continue

    sm = 0
    mx = a[0]
    for j in range(1, n):
        if (use_idx[j]):
            if a[j] <= mx:
                sm += mx-a[j]+1
                mx += 1
        mx = max(mx, a[j])
    res = min(sm, res)
print(res)

#3

from itertools import permutations
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

n_fact = 1
for i in range(1, n+1):
    n_fact *= i

sm = 0
for itr in permutations(xy):
    x, y = itr[0]
    dist = 0
    for nx, ny in itr[1:]:
        dist += ((nx-x)**2 + (ny-y)**2)**0.5
        x, y = nx, ny

    sm += dist

print(sm / n_fact)
