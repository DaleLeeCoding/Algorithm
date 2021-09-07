import sys
sys.stdin = open("/Users/seungwoolee/algorithm/Algorithm/Baekjoon/input.txt")
n = int(sys.stdin.readline().strip())
for _ in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))
    print(a+b)