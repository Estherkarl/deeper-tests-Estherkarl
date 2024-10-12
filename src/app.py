import os
from random import randrange

# function will return random number between start and end parameter where end is included
def rnd(start, end):
    return randrange(start, end+1)

# function should return the greatest number in a list
'''def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a < max:
            max = a
    return max
'''
#def rm(filename):
 #  os.remove(filename)


def rm(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} not found")
    os.remove(filename)


def max_num_in_list(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num
