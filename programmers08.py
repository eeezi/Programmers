def solution(s):
    comp = ""
    answer = []
    for x in s:
        num = comp.rfind(x)
        if num != -1:
            answer.append(len(comp)-num)
        else:
            answer.append(num)
        comp += x
        
    return answer