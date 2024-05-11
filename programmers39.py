def bonus(str):
    if str == "S" : return 1
    elif str == "D" : return 2
    elif str == "T" : return 3

def solution(dartResult):
    answer = []
    for i in range(len(dartResult)):
        try:
            if dartResult[i] == "1" and dartResult[i+1] == "0":
                score = 10**bonus(dartResult[i+2])
            else:
                score = int(dartResult[i])**bonus(dartResult[i+1])
            answer.append(score)
            
            if dartResult[i+2] == "*":
                if len(answer) == 1:
                    answer[-1] *= 2
                else:
                    answer[-1] *= 2
                    answer[-2] *= 2
                    
            elif dartResult[i+2] == "#":
                answer[-1] *= -1
                
        except:
            pass
    return sum(answer)
