import sys
sys.stdin = open("/Users/seungwoolee/algorithm/Algorithm/Baekjoon/input.txt")
N1, N2 = list(map(int, input().split()))
S1 = input()[::-1]
S2 = input()
T = int(input())
result = S1+S2
result_dic = dict()
for i in S1:
    result_dic[i] = 1 #positive direction
for j in S2:
    result_dic[j] = -1 #negative direction
print(result_dic)
for _ in range(T):
    temp = ''
    walker = 0
    while walker < len(result):
        if walker == len(result)-1: #only one left
            temp += result[walker]
            break
        first = result[walker]
        second = result[walker+1]
        if result_dic[first]*result_dic[second] == 1: #same direction
            temp += first
            walker += 1
        else:
            if result_dic[first] == -1: #arrival
                temp += first
                walker += 1

            else:
                temp += second
                temp += first
                walker += 2
    result = temp
print(result)


