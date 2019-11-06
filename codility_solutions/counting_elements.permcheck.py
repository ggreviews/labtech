def solution(A): 
    dictOfNumbers = { i : 1 for i in A }
    # Scan for duplicates 
    if len(A) != len(dictOfNumbers.keys()): 
        return 0 
    A.sort() 
    if len(A) == 1:
        return 1
    prev = A[0] 
    for k in range(1, len(A)): 
        #print("output ",A[k]) 
        if A[k] != ( prev + 1): 
            return 0 
        else: 
            prev = A[k] 
    return 1