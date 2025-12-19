# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 2025 3:44:33 PM

@author: Lim Jing
"""

import argparse
def main(args):
    input_data = []
    with open(args.input_file) as f:
        for line in f:
            row = []
            line = line.strip()
            try:
                for number in map(int, line.split()):
                    row.append(number)
                input_data.append(row)
            except ValueError:
                operators = line.split()
    cols = zip(operators, *input_data)

    part_a = 0
    for col in cols:
        op = col[0]
        if op == '+':
            result = 0
            for number in col[1:]:
                result += number
        elif op == '*':
            result = 1
            for number in col[1:]:
                result *= number
        part_a += result

    print(f'{part_a = }')

    input_data = []
    with open(args.input_file) as f:
        for line in f:
            row = []
            line = line.strip('\n')
            if line[0] != '+' and line[0] != '*':
                input_data.append(list(line))
            else:
                operators = line.split()[::-1]

    # transpose
    transposed_data = []
    grp = []
    for col_id in range(len(input_data[0])-1, -1, -1):
        col = ''
        for row in input_data:
            val = row[col_id]
            if val != ' ':
                col += val
        if col == '':
            transposed_data.append(grp)
            grp = []
        else:
            grp.append(int(col))
    transposed_data.append(grp)

    part_b = 0
    for op, grp in zip(operators, transposed_data):
        if op == '+':
            result = 0
            for num in grp:
                result += num
        elif op == '*':
            result = 1
            for num in grp:
                result *= num
        part_b += result

    print(f'{part_b = }')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    args = parser.parse_args()

    main(args)
