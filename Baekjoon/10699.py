import sys
sys.stdin = open("/Users/seungwoolee/algorithm/Algorithm/Baekjoon/input.txt")
n = int(sys.stdin.readline())
for _ in range(n):
    lst = list(sys.stdin.readline().split())
    result = 0
    for idx, elem in enumerate(lst):
        if idx == 0:
            result = float(elem)
        else:
            if elem == '@':
                result *= 3
            elif elem == '%':
                result += 5
            elif elem == '#':
                result -= 7
            else:
                print('error')
    print('%.2f' % result)
