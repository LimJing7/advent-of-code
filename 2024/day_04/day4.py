# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 22:23:43 2024

@author: Lim Jing
"""

inp_data = []
with open('input.txt') as f:
    for line in f:
        inp_data.append(list(line.strip()))


nrows = len(inp_data)
ncols = len(inp_data[0])
total = 0

# l2r + r2l
for row in inp_data:
    counters = []
    for j, col in enumerate(row[:-3]):
        if col == 'X' or col == 'S':
            counters.append(j)
    for c in counters:
        if row[c:c+4] == ['X','M','A','S'] or row[c:c+4] == ['S','A','M','X']:
            total += 1
print(f'{total = }')

# t2b + b2t
for j in range(ncols):
    counters = []
    for i in range(nrows-3):
        if inp_data[i][j] == 'X' or inp_data[i][j] == 'S':
            counters.append(i)
    for c in counters:
        if inp_data[c][j] == 'X' and inp_data[c+1][j] == 'M' and inp_data[c+2][j] == 'A' and inp_data[c+3][j] == 'S':
            total += 1
        elif inp_data[c][j] == 'S' and inp_data[c+1][j] == 'A' and inp_data[c+2][j] == 'M' and inp_data[c+3][j] == 'X':
            total += 1
print(f'{total = }')

# tl2br + br2tl
for i in range(nrows-3):
    counters = []
    for j in range(ncols-3):
        if inp_data[i][j] == 'X' or inp_data[i][j] == 'S':
            counters.append(j)
    for c in counters:
        if inp_data[i][c] == 'X' and inp_data[i+1][c+1] == 'M' and inp_data[i+2][c+2] == 'A' and inp_data[i+3][c+3] == 'S':
            total += 1
        if inp_data[i][c] == 'S' and inp_data[i+1][c+1] == 'A' and inp_data[i+2][c+2] == 'M' and inp_data[i+3][c+3] == 'X':
            total += 1
print(f'{total = }')

# tr2bl + bl2tr
for i in range(3, nrows):
    counters = []
    for j in range(ncols-3):
        if inp_data[i][j] == 'X' or inp_data[i][j] == 'S':
            counters.append(j)
    for c in counters:
        if inp_data[i][c] == 'X' and inp_data[i-1][c+1] == 'M' and inp_data[i-2][c+2] == 'A' and inp_data[i-3][c+3] == 'S':
            total += 1
        if inp_data[i][c] == 'S' and inp_data[i-1][c+1] == 'A' and inp_data[i-2][c+2] == 'M' and inp_data[i-3][c+3] == 'X':
            total += 1

print(f'{total = }')

cross_total = 0

# M . M
# . A .
# S . S
for i in range(nrows-2):
    for j in range(ncols-2):
        if inp_data[i][j] == 'M' and inp_data[i][j+2] == 'M' and inp_data[i+1][j+1] == 'A' and inp_data[i+2][j] == 'S' and inp_data[i+2][j+2] == 'S':
            cross_total += 1
print(f'{cross_total = }')

# M . S
# . A .
# M . S
for i in range(nrows-2):
    for j in range(ncols-2):
        if inp_data[i][j] == 'M' and inp_data[i][j+2] == 'S' and inp_data[i+1][j+1] == 'A' and inp_data[i+2][j] == 'M' and inp_data[i+2][j+2] == 'S':
            cross_total += 1
print(f'{cross_total = }')

# S . M
# . A .
# S . M
for i in range(nrows-2):
    for j in range(ncols-2):
        if inp_data[i][j] == 'S' and inp_data[i][j+2] == 'M' and inp_data[i+1][j+1] == 'A' and inp_data[i+2][j] == 'S' and inp_data[i+2][j+2] == 'M':
            cross_total += 1
print(f'{cross_total = }')

# S . S
# . A .
# M . M
for i in range(nrows-2):
    for j in range(ncols-2):
        if inp_data[i][j] == 'S' and inp_data[i][j+2] == 'S' and inp_data[i+1][j+1] == 'A' and inp_data[i+2][j] == 'M' and inp_data[i+2][j+2] == 'M':
            cross_total += 1
print(f'{cross_total = }')
