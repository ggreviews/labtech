# Detected time complexity: O(N) or O(N * log(N))

def solution(A):    
    delete_key = dict.fromkeys(range(1, (len(A)+2) ))    
    for item in A:
        del delete_key[item]
    retvalue = 1
    for key in delete_key.keys():
        retvalue = key    
    return key