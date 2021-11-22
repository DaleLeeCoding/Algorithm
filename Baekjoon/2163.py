#https://www.acmicpc.net/problem/2163
import sys
sys.stdin = open("./input.txt", "r")
n, m = map(int, sys.stdin.readline().strip().split())
print(n*m-1)

