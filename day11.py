#1

a. b = map(int, input().split())
load_area = (1*a+1*b)-(1*1)
print(load_area)

#2

from math import sqrt
n = int(input())
ans = 0
for i in range(1, n+1):
    counter = 0
    for j in range(1, int(sqrt(i))+1):
        if i%j == 0 and i%2 == 1:
            counter += 1
    if counter == 4:
        ans += 1
print(ans)

#3

s = input()
k = int(input())
for i, c in enumerate(s):
    if i == k-1:
        print(c)
        break
    if c != "1":
        print(c)
        break

#4

N, M, Q = map(int, input().split())
lr = [[0]*(N+1) for _ in range(N+1)]
for m in range(M):
    l, r = map(int, input().split())
    lr[l][r] += 1
P = [list(map(int, input().split())) for _ in range(Q)]
csum = []
for i in range(N+1):
    List = [0]
    for e in range(len(lr[i])):
        List.append(List[e]+lr[i][e])
    csum.append(List)
for p in P:
    ans = 0
    l, r = p
    for c in csum[l:r+1]:
        ans += (c[r+1]-c[l])
    print(ans)

#5

h, w = map(int, input().split())
a_list = [list(input()) for _ in range(h)]
dot_cnt = [sum(a == "." for a in a_col) for a_col in a_list]
exist_idx = [i for i, num in enumerate(dot_cnt) if num != w]
st = set(range(w))
for i in exist_idx:
    dot_idx = [i for i, a in enumerate(a_list[i]) if a == "."]
    st = st & set(dot_idx)
for i in exist_idx:
    print("".join([a for i,a in enumerate(a_list[i]) if i not in st]))


    
