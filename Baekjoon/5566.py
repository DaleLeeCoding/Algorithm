import sys
sys.stdin = open("/Users/seungwoolee/algorithm/Algorithm/Baekjoon/input.txt")
n, m = map(int, sys.stdin.readline().split())
data = []
now, cnt = 0, 0
for _ in range(n):
    data.append(int(sys.stdin.readline().strip()))

for _ in range(m):
    now += int(sys.stdin.readline().strip())
    cnt += 1
    if now >= n:
        print(cnt)
        exit()
    else:
        now += data[now]
        if now >= n:
            print(cnt)
            exit()
print(cnt)