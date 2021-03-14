n, k = map(int, input().split())
d = list(map(int, input().split()))
c_u_n = []
min_yen = float('inf')
for i in range(10):
    if not i in d:
        c_u_n.append(str(i))
for i in range(n, 10000):
    yen = list(str(i))
    flg = True
    for j in range(len(yen)):
        if not yen[j] in c_u_n:
            flg = False
            break
    if flg:
        min_yen = min(min_yen, i)
        break
print(min_yen)
        
