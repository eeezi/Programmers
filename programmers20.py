def solution(number, limit, power):
    answer = 0
    cnt = [0] * (number + 1)

    for x in range(1, number + 1):
        for y in range(x, number + 1, x):
            cnt[y] += 1

    for x in range(1, number + 1):
        if cnt[x] > limit:
            answer += power
        else:
            answer += cnt[x]

    return answer