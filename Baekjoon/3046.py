#https://www.acmicpc.net/problem/3046
import sys
sys.stdin = open("./input.txt", "r")
r1, s = map(int, sys.stdin.readline().strip().split())
print(2*s-r1)

