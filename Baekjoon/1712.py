import sys
sys.stdin = open("/Users/seungwoolee/algorithm/Algorithm/Baekjoon/input.txt")

a, b, c = list(map(int, input().split()))
if b >= c:
    print(-1)
else:
    n = a//(c-b)+1
    print(n)