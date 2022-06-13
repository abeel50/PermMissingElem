def solution(A):
    # write your code in Python 3.6
    m = len(A) + 1
    return (m * (m  + 1 ))//2 - sum(A)