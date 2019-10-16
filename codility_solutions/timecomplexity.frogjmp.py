# rough solution- needs to be optimised for big jumps

# def solution(X, Y, D):
    # start = X
    # end = Y
    # jump_distance = D
    # jump_so_far = 0
    # while True:
        # jump_so_far = jump_so_far+1
        # distance_covered = start + jump_distance*jump_so_far
        # if(distance_covered > end):
            # break
    # return jump_so_far
    
# Optimised using mathematics
    
import math

def solution(X, Y, D):
    Z = Y - X
    return math.ceil(Z/D)    
