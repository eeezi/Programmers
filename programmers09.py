def solution(strings, n):
    strings = sorted(strings)

    return sorted(strings, key=lambda strings: strings[n])