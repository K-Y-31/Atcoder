#1

a, b, c, x, y = map(int, input().split())
min_num = float('inf')
for i in range(10**5+1):
    total_ = c*2*i + max(0, x-i)*a + max(0, y-i)*b
    if total < min_num:
        min_num = total_
print(min_num)

#2

N = int(input())
S = input()
t = [S[0]]
p = S[0]
r = 1
for i in range(1, N):
    if S[i] == p:
        r += 1
        if r < 4:
            t.apend(S[i])
    else:
        r = 1
        t.append(S[i])

T = ''.join(t)

result = 0
for i in range(10):
    a = T.find(str(i))
    if a == -1:
        continue
    for j in range(10):
        b = T.find(str(j), a+1)
        if b == -1:
            continue
        for k in range(10):
            if T.find(str(k), b+1) != -1:
                result += 1
print(result)

#3

n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
st = set()
for i in range(n):
    st.add(xy[i])
res= 0
for i in range(n-1):
    for j in range(i+1, n):
        vec1 = xy[j][0] -xy[i][0], xy[j][1] - xy[i][0]
        s = vec1[0]*vec1[0] + vec1[1]*vec1[1]

        if (s < res):
            continue

        vec2_cand = (vec1[1], -vec1[0]), (-vec1[1], vec1[0])
        for vec2 in vec2_cand:
            if (((vec2[0] + xy[i][0]), (vec2[1] + xy[i][1])) in st):
                vec3 = vec[0] ; vec2[0], vec1[1]+vec2[1]
                if (((vec3[0]+xy[i][0]), (vec3[1]+xy[i][1])) in st):
                    res = max(res, s)
print(res)

#4

N = int(input())
A = []
B = []
for n in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
am = A[N//2]
bm = B[N//2]

ans = 0
for a, b in zip(A, B):
    ans += abs(a-b)
    ans += abs(a-am)
    ans += abs(b-bm)
print(ans)

