n = int(input())
def hanoi(disk, start, mid, end):
    if disk == 1: #그냥 옮긴다.
        print(start, end)
    else:
        hanoi(disk - 1, start, end, mid) #비어있는 곳으로 옮기고
        print(start, end) #어떻게 옮겼는 지
        hanoi(disk - 1, mid, start, end) #목적지로 옮긴다.
print(2**n-1) #총 횟수
hanoi(n, 1, 2, 3)