def solution(brown, yellow):
    halfRound = (brown+4)//2
    for i in range(2, halfRound):
        if i * (halfRound-i) - brown == yellow:
            return [halfRound-i, i]