# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:30:09 2024

@author: Lim Jing
"""

import re

inp_data = []
with open('input.txt') as f:
    for line in f:
        inp_data.append(line.strip())

total_sum = 0
for line in inp_data:
    matches = re.findall(r'mul\(\d+,\d+\)', line)
    for matched in matches:
        i, j = matched[4:-1].split(',')
        prod = int(i)*int(j)
        total_sum += prod

print(f'{total_sum = }')

enabled_sum = 0
disabled = False
for line in inp_data:
    matches = re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", line)
    for matched in matches:
        if matched[0] != '':
            curr = matched[0]
        elif matched[1] != '':
            curr = matched[1]
        elif matched[2] != '':
            curr = matched[2]
        else:
            print('????')
        if curr == 'do()':
            disabled = False
        elif curr == 'don\'t()':
            disabled = True
        else:
            if not disabled:
                i, j = curr[4:-1].split(',')
                prod = int(i)*int(j)
                enabled_sum += prod

print(f'{enabled_sum = }')
