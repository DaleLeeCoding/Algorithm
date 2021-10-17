#https://www.acmicpc.net/problem/1316
import sys
sys.stdin = open("/Users/seungwoolee/algorithm/Algorithm/Baekjoon/input.txt")

n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    temp = word[0]
    lst = []
    for i in word:
        if i == temp:
            continue
        else:
            if i in lst:
                cnt -= 1
                break
            else:
                lst.append(temp)
                temp = i
    cnt += 1
print(cnt)