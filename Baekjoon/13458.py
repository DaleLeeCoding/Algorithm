#https://www.acmicpc.net/problem/13458
import sys
import math
sys.stdin = open("./input.txt", 'r')
N = int(input())
A = list(map(int, input().split()))
B, C = list(map(int, input().split()))
cnt_all = 0
for elem in A:
   cnt_room = max(0, math.ceil((elem-B)/C)) + 1
   cnt_all += cnt_room
print(cnt_all)
