import sys
sys.stdin = open("G:/내 드라이브/algorithm/Algorithm/Baekjoon/input.txt", "r")

#https://www.acmicpc.net/problem/1912
n = int(input())
numbers = list(map(int, input().split()))
print('n:', n)
print('numbers: ', numbers)
max_num = max(numbers)
print(max_num)