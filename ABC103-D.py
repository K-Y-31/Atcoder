#abc 103-d

n,m = map(int, input().split())
dispute = []
for i in range(m):
    a, b = map(int, input().split())
    dispute.append((b, a))
dispute.sort()
ans = 0
most_right_bridge = 0
for b, a in dispute:
    if most_right_bridge <= a:
        ans += 1
        most_right_bridge = b
print(ans)
