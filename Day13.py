n, x = map(int, input().split())
x_ = list(map(int, input().split()))
x_d = []
for e in x_:
    x_d.append(abs(x-e))

def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

d = x_d[0]
for e in x_d[1:]:
    d = gcd(d, e)
print(d)

h, w = map(int, input().split())
relation = []
for i in range(h):
    if i%2 == 0:
        relation.extend((i, j) for j in range(w))
    else:
        relation.extend((i, j) for j in range(w-1, -1, -1))
field = [list(map(int, input().spolit())) for _ in range(h)]
buf = []
fir (i1, j1), (i2, j2) in zip(relaiton, relation[1:]):
    if field[i1][j1] % 2 == 1:
        field[i1][j1] -= 1
        field[i2][j2] += 1
        buf.append((i1+1, j1+1, i2+1, j2+1))
print(len(buf))
print('\n'.join(''.join(map(str, line)) for line in buf))
