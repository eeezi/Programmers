def solution(s):
    answer = []
    for x in s:
        if x == "(":
            answer.append(x)
        else:
            try:
                answer.pop()
            except:
                return False
    return not answer