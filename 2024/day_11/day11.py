# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 09:37:46 2024

@author: Lim Jing
"""

with open('input.txt') as f:
    l = f.readline().strip().split()
    input_nums = list(map(int , l))

memo_dict = {}

def blink(x):
    if x == 0:
        return 1,
    if len(str(x)) % 2 == 0:
        x1 = int(x // (10**(len(str(x))/2)))
        x2 = int(x % (10**(len(str(x))/2)))
        return (x1, x2)
    return x * 2024,

def blinks(x, times):
    if (x, times) in memo_dict:
        return memo_dict[(x, times)]
    if times == 0:
        memo_dict[(x,times)] = 1
        return 1
    o = blink(x)
    n_stones = 0
    for v in o:
        n_stones += blinks(v, times-1)
    memo_dict[(x,times)] = n_stones
    return n_stones

print(f'{sum(map(lambda x: blinks(x, 25), input_nums))}')
print(f'{sum(map(lambda x: blinks(x, 75), input_nums))}')
