#1

from sys import exit
SM = []
SN = []
M = int(input())
for m in range(M):
    x, y = map(int, input().split())
    XM.append((x, y))
N = int(input())
for n in range(N):
    x, y = map(int, input().split())
    SN.append((x, y))
st = set()
base = SM[0]
for sn in SN:
    dx, dy = sn[0]-base[0], sn[1]-base[1]
    ok = True
    for sm in SM:
        if not (sm[0]+dx, sm[1]+dy) in st:
            ok = False
            break
    if ok:
        print(dx, dy)
        exit()

#2

n = int(input())
a = list(map(int, input().split()))
st = set()
for i in range(2**n):
    sm = 0
    for j in range(n):
        if (i&(1 << j)):
            sm += a[j]
    st.add(sm)
q = int(input())
m = list(map(int, input().split()))

for i in range(q):
    if m[i] in st:
        print('yes')
    else:
        print('no')



#3

n,m = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))
res = 0
for i in range(2**n):
    on = [0 for _ in range(n)]
    for j in range(n):
        if (i&(1<<j)):
            on[j] = 1
    all_on = True
    for j in range(m):
        on_num = 0
        for s in ks[j][1:]:
            if (on[s-1]):
                on_nun += 1
        if (on_num%2 != p[j]):
            all_on = False
            break
    if all_on:
        res += 1
print(res)

#4

n,m = map(int, input().split())
relations = set()
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    relations.add((x, y))
res = 0
for i in range(2**n):
    num = 0
    faction = []
    for j in range(n):
        if (i & (1 << j)):
            faction.append(j)
            num += 1
    if num < res:
        continue
    flg = True
    for j in range(num-1):
        for i in range(j+1, num):
            relation = faction[j], faction[i]
            if not relation in relations:
                flg = False
                break
        if not flg:
            break
    if flg:
        res = max(res, num)
print(res)
            
                
            
