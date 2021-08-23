import sys
sys.stdin = open("/Users/seungwoolee/algorithm/Algorithm/Baekjoon/input.txt")

#https://www.acmicpc.net/problem/1912
n = int(input())
numbers = list(map(int, input().split()))

#첫 시작
result_lst = []
#값을 담을 바구니
basket = 0

for i in range(len(numbers)):
    basket += numbers[i]
    if numbers[i] > 0:
        result_lst.append(basket)
    else:
        if basket < 0: #담아봤자 손해
            basket = 0 #다 버린다.

if result_lst == []: #음수밖에 없을 때
    print(max(numbers))
else:
    print(max(result_lst))
        
