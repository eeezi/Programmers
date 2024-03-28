from collections import Counter

def solution(X, Y):
    answer = []
    counter_X = Counter(X)
    counter_Y = Counter(Y)

    numbers = counter_X & counter_Y

    if not numbers:
        return "-1"

    for num, count in sorted(numbers.items(), reverse=True):
        answer.extend([num] * count)
        
    if answer.count("0") == len(answer):
        return "0"

    return "".join(answer)