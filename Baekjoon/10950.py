import sys
sys.stdin = open("/Users/seungwoolee/algorithm/Algorithm/Baekjoon/input.txt")

n = int(input())
for _ in range(n):
    a, b = list(map(int, input().split()))
    print(a+b)
