#1

h, w, a, b = map(int, input().split())

def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n-r)
    return fact[n]*factinv[r]*factinv[n-r]%mod

N = 2*10**5+1000
mod = pow(10, 9) + 7
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N+1):
    fact.append((fact[-1]*i)%mod)
    inv.append((-inv[mod%i]*(mod//i))%mod)
    factinv.append((factinv[-1]*inv[-1])%mod)

#2

ans = 0
for i in range(h-a):
    ans += cmb((b-1+i, i)*cmb(w-b-1+h-i-1, w-b-1))%(10**9+7)

print(ans%(10**9+7))


#3
a, b = map(int, input().split())
if a <= 8 and b <= 8:
    print('Yay!')
else:
    print(':(')


#4

n = int(input())
a_row = list(map(int, input().split()))
total = 0

for i in range(n):
    while a_row[i]%2 == 0:
        ans += 1
        a_row[i] //= 2
print(ans)

#5

n,m = map(int, input().split())
xyz = [list(map(int, input().split())) for i in range(n)]
ans = []
for i in [-1, 1]:
    for j in [-1, 1]:
        for s in [-1, 1]:
            ans.append(sum(sorted([i*l[0]+j*l[1]+s*l[2] for l in xyx], reverse=True)[:m]))
print(ans)
    

