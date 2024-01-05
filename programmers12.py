def solution(n, arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        answer.append(bin(x|y)[2:].zfill(n).replace("0"," ").replace("1","#"))
    return answer