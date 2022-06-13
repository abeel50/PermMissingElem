def solution(A):
    # write your code in Python 3.6
    m = max(A)
    return (m * (m  + 1 ))//2 - sum(A)