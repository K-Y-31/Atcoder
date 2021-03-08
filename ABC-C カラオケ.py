N, M = map(int, input().split())
student_point = [list(map(int, input().split())) for _ in range(N)]
res = 0
for i in range(M):
    for j in range(M):
        sum = 0
        for c in range(N):
            sum += max(student_point[c][i], student_point[c][j])
        res = max(res, sum)
print(res)
