def solution(lottos, win_nums):
    win = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    count = 0
    zero = 0
    for lotto in lottos:
        if lotto in win_nums:
            count += 1
        elif lotto == 0:
            zero += 1
    return [win[count+zero], win[count]]