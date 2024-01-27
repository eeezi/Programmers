def solution(d, budget):
    if sum(d) == budget:
        return len(d)
    while sum(d) > budget:
        d.pop(d.index(max(d)))
    return len(d)