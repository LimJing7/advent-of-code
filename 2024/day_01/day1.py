# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:41:40 2024

@author: Lim Jing
"""

list1 = []
list2 = []

with open('input.txt') as f:
    for line in f:
        a,b = line.strip().split()
        list1.append(int(a))
        list2.append(int(b))

list1.sort()
list2.sort()

total_diff = 0
for i, j in zip(list1, list2):
    total_diff += abs(i-j)

print(f'{total_diff = }')


sim_score = 0
start_idx = 0
for i in list1:
    for j in list2[start_idx:]:
        if j > i:
            break
        elif j == i:
            sim_score += j
        else:
            start_idx += 1

print(f'{sim_score = }')
