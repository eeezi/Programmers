def solution(name, yearning, photo):
    answer = []
    for people in photo:
        score = 0
        for x, y in zip(yearning, name):
            if y in people:
                score += x
        answer.append(score)
    return answer