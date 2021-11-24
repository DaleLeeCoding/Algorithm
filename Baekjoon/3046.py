#https://www.acmicpc.net/problem/3046
import sys
sys.stdin = open("./input.txt", "r")
n, m = map(int, sys.stdin.readline().strip().split())
print(n*m-1)