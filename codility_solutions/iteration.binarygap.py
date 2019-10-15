#!/var/bin/env python
# Richard Lee October 2019

import re

def solution(N):
    binary_string = bin(N)
    split_binary_list = binary_string.split("1")
# Delete first entry
    del split_binary_list[0]
#If last entry contains zeroes, delete it    
    prog = re.compile('^0+$')
    if prog.match(split_binary_list[-1]):
        del split_binary_list[-1]
    biggest = 0
    if not split_binary_list:
        return 0
    else:
        for entry in split_binary_list:
            if len(entry) > biggest:
                biggest = len(entry)
    return biggest