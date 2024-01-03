def solution(s):
    word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i, x in enumerate(word):
        s = s.replace(x, str(i))
        
    return int(s)