import sys
sys.stdin = open("/Users/seungwoolee/algorithm/Algorithm/Baekjoon/input.txt")

#초기 세팅
n = int(input())
numbers = []
dp = [-1]*n
for i in range(n):
    numbers.append(int(input()))

#n이 1,2,3인 경우를 elif 말고 더 깔끔하게 짤 수 있을까요?.?
if n == 1:
    print(numbers[0])
elif n == 2:
    print(numbers[0]+numbers[1])
elif n == 3:
    print(max(numbers[0]+numbers[2], numbers[1]+numbers[2]))
else: #마지막으로 가는 방법은 3번째 전에서 2칸, 1칸을 이동하는 경우와 2번째 전에서 2칸을 이동하는 경우가 있으므로 이를 비교합니다.
    dp[0] = numbers[0]
    dp[1] = numbers[0]+numbers[1]
    dp[2] = max(numbers[0]+numbers[2], numbers[1]+numbers[2])
    for j in range(3, n):
        dp[j] = max(dp[j-3]+numbers[j-1]+numbers[j], dp[j-2] + numbers[j])
    print(dp[n-1])
