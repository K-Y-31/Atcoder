#1

n,x = map(int, input().split())
counter = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        for s in range(j+1, n+1):
            if i+j+s==x:
                counter += 1

print(counter)

#2

import itertools
n = int(input())
p = [int(i)-1 for i in input().split()]
q = [int(i)-1 for i in input().split()]
m = sorted(p)
a = 0
b = 0
cnt = 1
for i in itertools.permutations(m):
    if list(i) == p:
        a += cnt
    if list(i) == q:
        b += cnt
    if a != 0 and b != 0:
        break
    else:
        cnt += 1
print(abs(a-b))

#3

from itertools import permutations
K = int(input())
N = 8
RC = []
for k in range(K):
    r, c = map(int, input().split())
    RC.append((r, c))


def diag(board):
    for i in range(2*N-1):
        sm = 0
        for j in range(i+1):
            if (i-j>=8 or j >= 8):
                continue
            sm += board[i-j][i]
        if sm > 1:
            return False
    return True

def judge(ls):
    board = [[0]*N for _ in range(N)]
    for r in range(N):
        c = ls[r]
        board[r][c] = 1
    for r,c in RC:
        if board[r][c] == 0:
            return False

    if not diag(board):
        return False

    if not diag(board[::-1]):
        return False
    return True

for ls in permutations(range(N)):
    if judge(ls):
        for c in ls:
            s = ['.']*N
            s[c] = 'Q'
            print(''.join(s))
            
