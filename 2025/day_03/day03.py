# -*- coding: utf-8 -*-
"""
Created on Sun Dec 07 2025 11:47:11 AM

@author: Lim Jing
"""

import argparse
from functools import reduce

def main(args):
    ratings = []
    with open(args.input_file) as f:
        for line in f:
            bank = line.strip()
            ratings.append(list(map(int, bank)))

    part_a = 0
    for bank in ratings:
        curr_max = 0
        curr_pos = 0
        for pos, batt in enumerate(bank[:-1]):
            if batt > curr_max:
                curr_max = batt
                curr_pos = pos

        max2 = 0
        for pos in range(curr_pos+1, len(bank)):
            if bank[pos] > max2:
                max2 = bank[pos]

        part_a += curr_max*10 + max2

    print(f'{part_a = }')

    part_b = 0
    for bank in ratings:
        start_pos = 0
        selected = []
        for reserved_digit in range(12-1, -1, -1):
            curr_max = 0
            curr_pos = start_pos
            for pos in range(start_pos, len(bank)-reserved_digit):
                if bank[pos] > curr_max:
                    curr_max = bank[pos]
                    curr_pos = pos
            selected.append(curr_max)
            start_pos = curr_pos+1
        sel_bank = reduce(lambda x,y: x*10+y, selected, 0)
        part_b += sel_bank

    print(f'{part_b = }')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    args = parser.parse_args()

    main(args)
