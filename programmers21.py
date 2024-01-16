def solution(n, m, section):
    answer = 1
    wall = section[0]
    for i in range(1, len(section)):
        if section[i] - wall >= m:
            answer += 1
            wall = section[i]
    return answer 