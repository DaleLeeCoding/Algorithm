import sys
sys.stdin = open("/Users/seungwoolee/algorithm/Algorithm/Baekjoon/input.txt")
#https://www.acmicpc.net/problem/3986
n = int(input())
cnt = 0 #count
for _ in range(n):
    word = input()
    if word.count('A') % 2 == 1 or word.count('B') % 2 == 1: #하나가 남는다.
        continue
    else:
        stack = []
        for c in word:
            if len(stack) == 0 or stack[-1] != c: #빈 스택이거나 스택의 마지막이 다른 경우
                stack.append(c) #스택에 추가해준다.
            else: #만일 스택의 마지막과 같은 경우 같이 없애준다!
                stack.pop()
        if len(stack) == 0: #다 끝난 뒤 스택이 비었으면 좋은 단어
            cnt += 1
        else:
            continue
print(cnt)
