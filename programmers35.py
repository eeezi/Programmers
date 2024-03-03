import math
def solution(n, words):
    answer = []

    for i, word in enumerate(words):
        if word not in answer:
            if answer and answer[-1][-1] != word[0]:
                return [i%n+1, math.ceil((i+1)/n)]
            answer.append(word)
        else:
            return [i%n+1, math.ceil((i+1)/n)]
    return [0, 0]