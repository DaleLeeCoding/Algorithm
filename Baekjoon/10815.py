#https://www.acmicpc.net/problem/10815

import sys
sys.stdin = open("/Users/seungwoolee/algorithm/Algorithm/Baekjoon/input.txt")

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
check_num = int(input())
check_numbers = list(map(int, input().split()))
lst = []

def binary_search(num, start, end):
    while start <= end:
        mid = (start + end) // 2
        if num==numbers[mid]:
            lst.append('1')
            return
        elif num < numbers[mid]:
            end = mid-1
        else:
            start = mid+1
    lst.append('0')
    return

for number in check_numbers:
    start = 0
    end = n-1
    binary_search(number, start, end)

print(" ".join(lst))