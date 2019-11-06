def solution(X, A):
    solution_dict = {}
    current_time = -1
    if len(A) == 1:
        if A[0] == 1:
            return 0
        else:
            return -1
    
    for i in range(0, len(A)): 
        #print("{i} is {item}".format(i=i,item=A[i]))
        if A[i] <= X:
            solution_dict[A[i]] = 1
        #print("length dict {le}".format(le=len(solution_dict.keys())))
        if len(solution_dict.keys()) == X: 
            current_time = i
            break
    return current_time