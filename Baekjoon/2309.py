import sys
from itertools import combinations
sys.stdin = open("./input.txt", "r")
data = [int(sys.stdin.readline().strip()) for _ in range(9)]
data.sort()
sum_data = sum(data)
for i, j in list(combinations(data, 2)):
    if i + j == sum_data - 100:
        for k in data:
            if k != i and k != j:
                print(k)
        break