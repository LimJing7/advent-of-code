# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 22:08:55 2024

@author: Lim Jing
"""

inp_data = []
with open('input.txt') as f:
    for line in f:
        line_list = line.strip().split()
        line_list = [int(i) for i in line_list]
        inp_data.append(line_list)

def check_report(report: list[int]) -> tuple[bool, int]:
    if report[0] < report[1]:
        increasing = True
    else:
        increasing = False

    prev = report[0]
    for i, lvl in enumerate(report[1:]):
        if increasing:
            if lvl <= prev:
                return False, i+1
        else:
            if lvl >= prev:
                return False, i+1
        diff = abs(lvl-prev)
        if diff < 1 or diff > 3:
            return False, i+1
        prev = lvl

    return True, -1

safe_reports = 0
safe_damped_reports = 0
for report in inp_data:
    safe, unsafe_lvl = check_report(report)
    if safe:
        safe_reports += 1
        safe_damped_reports += 1
    else:
        if check_report(report[:unsafe_lvl]+report[unsafe_lvl+1:])[0]:
            safe_damped_reports += 1
        elif check_report(report[:unsafe_lvl-1]+report[unsafe_lvl:])[0]:
            safe_damped_reports += 1
        elif check_report(report[1:])[0]:  # need to check this when there's an inversion at index 2
            safe_damped_reports += 1

print(f'{safe_reports = }')
print(f'{safe_damped_reports = }')
