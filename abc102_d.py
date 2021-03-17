#equal cut


n = int(input())
a = list(map(int, input().split()))

res = float('inf')
s_m = [0]
for i in range(n):
    s_m.append(s_m[i] + a[i])

for i in range(n):
    low = 0
    high = i
    while high - low > 1:
        mid = (high + low)//2
        if s_m[mid] >= s_m[i] - s_m[mid]:
            high = mid - 1
        else:
            low = mid + 1
    p, q = s_m[low], s_m[i] - s_m[low]
    p2, q2 = s_m[high], s_m[i]  - s_m[high]
    left_min, left_max = min(p, q), max(p, q)
    if abs(p2-q2) < abs(p-q):
        left_min, left_max = min(p2, q2), max(p2, q2)
    
    low = i,
    high = n
    while high - low > 1:
        mid = (high + low) // 2
        if s_m[mid] - s_m[i] >= s_m[n] - s_m[mid]:
            high = mid - 1
        else:
            low = mid + 1
    r, s = s_m[low] - s_m[i], s_m[n] - s_m[low]
    r2, s2 = s_m[high] - s_m[i], s_m[n] - s_m[high]
    right_min, right_max = min(r, s), max(r, s)
    if abs(r2-s2) < abs(r-s):
        right_min, right_max = min(r2, s2), max(r2, s2)
    
    tmp = max(left_max, right_max) - min(left_min ,  right_min)
    res = min(res, tmp)

print(res)
