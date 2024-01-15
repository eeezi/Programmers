def solution(s):
    s = s.lower()
    str = list(s)
    if str[0].isalpha():
        str[0] = str[0].upper()
        
    for i in range(1, len(str)):
        if (str[i-1] == " ") and (str[i].isalpha()):
            str[i] = str[i].upper()
    return "".join(str)
