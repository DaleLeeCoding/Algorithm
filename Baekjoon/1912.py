import sys
sys.stdin = open("../input.txt", "r")

n = int(input())
numbers = list(map(int, input().split()))
print('n:', n)
print('numbers: ', numbers)