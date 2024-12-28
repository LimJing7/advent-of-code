# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 10:15:11 2024

@author: Lim Jing
"""

with open('input.txt') as f:
    for line in f:
        inp = line.strip()

f_sizes = []
emp_sizes = []

for i, val in enumerate(inp):
    if i%2 == 0:
        f_sizes.append(int(val))
    else:
        emp_sizes.append(int(val))

front_idx = 0
back_idx = len(inp) - 1

back_file_idx = len(f_sizes) - 1
cursor_pos = 0

total = 0
while front_idx <= back_idx:
    if front_idx % 2 == 0:  # file location
        cur_file_idx = front_idx//2
        cur_file_size = f_sizes[cur_file_idx]
        for i in range(cur_file_size):
            total += (cursor_pos+i) * cur_file_idx
        cursor_pos += cur_file_size
        front_idx += 1

    else:  # empty location
        cur_file_idx = back_file_idx
        cur_file_rem_size = f_sizes[cur_file_idx]
        cur_emp_idx = front_idx//2
        cur_emp_size = emp_sizes[cur_emp_idx]

        if cur_emp_size < cur_file_rem_size:
            for i in range(cur_emp_size):
                total += (cursor_pos+i) * cur_file_idx
            cursor_pos += cur_emp_size
            f_sizes[cur_file_idx] -= cur_emp_size
            emp_sizes[cur_emp_idx] = 0
            front_idx += 1
        elif cur_emp_size == cur_file_rem_size:
            for i in range(cur_emp_size):
                total += (cursor_pos+i) * cur_file_idx
            cursor_pos += cur_emp_size
            f_sizes[cur_file_idx] = 0
            emp_sizes[cur_emp_idx] = 0
            front_idx += 1
            back_file_idx -= 1
        else:
            for i in range(cur_file_rem_size):
                total += (cursor_pos+i) * cur_file_idx
            cursor_pos += cur_file_rem_size
            f_sizes[cur_file_idx] = 0
            emp_sizes[cur_emp_idx] -= cur_file_rem_size
            back_file_idx -= 1
    back_idx = back_file_idx * 2
    # print(f'{cursor_pos-1}: {total}')

print(f'{total = }')


## part b

files = {}  # f_idx:(start, size)
empty = {}  # start: size

cursor_pos = 0
for i, val in enumerate(inp):
    val = int(val)
    if i%2 == 0:
        files[i//2] = (cursor_pos, val)
        cursor_pos += val
    else:
        empty[cursor_pos] = val
        cursor_pos += val

n_files = len(files)

for f_idx in range(n_files-1, 0, -1):  # f_idx 0 doesn't need to move
    cur_pos, size = files[f_idx]
    for i in range(cur_pos):
        if i in empty:
            if empty[i] >= size:
                orig_space = empty.pop(i)
                new_space = orig_space - size
                if new_space > 0:
                    empty[i+size] = new_space
                files[f_idx] = (i, size)  # aft moving new empty is created but ignored because we move from right to left
                break

total_b = 0
for f_idx, (start_pos, size) in files.items():
    for i in range(size):
        total_b += f_idx * (start_pos+i)

print(f'{total_b = }')
