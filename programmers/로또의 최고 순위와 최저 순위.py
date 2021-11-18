#https://programmers.co.kr/learn/courses/30/lessons/77484
#로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    plus = lottos.count(0)
    answer = len(list(set(lottos) & set(win_nums))) 
    result = [7-answer-plus, 7-answer]
    for i in range(len(result)):
        if result[i] == 7:
            result[i] -= 1
    return result
