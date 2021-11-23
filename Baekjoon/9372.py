import sys
sys.stdin = open("/Users/seungwoolee/algorithm/Algorithm/Baekjoon/input.txt")
T= int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, M = list(map(int, sys.stdin.readline().rstrip().split()))
    print(N-1)
    for i in range(M):
        start, end = list(map(int, sys.stdin.readline().rstrip().split()))
        pass
