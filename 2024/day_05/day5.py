# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:02:31 2024

@author: Lim Jing
"""

from collections import defaultdict
from functools import cmp_to_key

prior_dict = defaultdict(set)
after_dict = defaultdict(set)
ill_prior_dict = defaultdict(set)
ill_after_dict = defaultdict(set)

rules = []
with open('input.txt') as f:

    for line in f:
        if '|' in line:
            a, b = line.strip().split('|')
            prior_dict[int(b)].add(int(a))
            after_dict[int(a)].add(int(b))
            ill_after_dict[int(b)].add(int(a))
            ill_prior_dict[int(a)].add(int(b))
        elif line == '\n':
            continue
        else:
            rules.append(list(map(int, line.strip().split(','))))

def check(rule):
    for i, val_i in enumerate(rule):
        for val_j in rule[i:]:
            if val_j in ill_after_dict[val_i]:
                return False
    return True


def my_helpful_cmp(a, b):
    if b in after_dict[a]:
        return -1
    elif a in after_dict[b]:
        return 1
    else:
        return 0

def fix(rule):
    return sorted(rule, key=cmp_to_key(my_helpful_cmp))


mid_total = 0
fixed_total = 0
for rule in rules:
    if check(rule):
        mid_total += rule[len(rule)//2]
    else:
        fixed_total += fix(rule)[len(rule)//2]

print(f'{mid_total = }')
print(f'{fixed_total = }')
