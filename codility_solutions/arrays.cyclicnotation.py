# https://stackoverflow.com/questions/9457832/python-list-rotation
def rotate(l, n):
    return l[-n:] + l[:-n]

def solution(A, K):
    return rotate(A, K)