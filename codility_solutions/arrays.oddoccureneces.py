# Richard Lee October 2019

def solution(A):
    result_hash = {}
    for item in A:
        if item in result_hash:
            del result_hash[item]
        else:
            result_hash[item] = 1
    odd_one = 0
    for item in result_hash.keys():
        odd_one = item
    return odd_one