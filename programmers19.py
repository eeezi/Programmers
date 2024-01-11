def solution(answers):
    supoja1 = [1,2,3,4,5] * (len(answers)//5+1)
    supoja2 = [2,1,2,3,2,4,2,5] * (len(answers)//8+1)
    supoja3 = [3,3,1,1,2,2,4,4,5,5] * (len(answers)//10+1)
    answer = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == supoja1[i]: answer[0] += 1
        if answers[i] == supoja2[i]: answer[1] += 1
        if answers[i] == supoja3[i]: answer[2] += 1

    return [i+1 for i, x in enumerate(answer) if x==max(answer)]

# cycle이라는 함수도 있던데 string을 *로 늘리는 방법 말고 cycle 사용해서 늘리는 방법 생각해보기