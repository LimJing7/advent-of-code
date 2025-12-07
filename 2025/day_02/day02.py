# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 18:04:45 2025

@author: Lim Jing
"""

import argparse
import re

def main(args):
    with open(args.input_file) as f:
        a = f.readline()

    ranges = [pair.split('-') for pair in a.strip().split(',')]

    part_a = 0
    part_b = 0

    for (s, e) in ranges:
        lower = int(s)
        upper = int(e) + 1
        e = str(upper)
        if len(s) == len(e):
            if len(s) % 2 == 1:
                continue
            half_len = len(s) // 2
            first_half = int(s[:half_len])
            for x in range(first_half, int('9'*half_len)+1):
                test_id = x*10**half_len + x
                if test_id >= lower and test_id < upper:
                    part_a += test_id
                else:
                    continue
        else:
            order = len(e) - len(s)
            if len(s) % 2 == 1:
                order -= 1
                s = '1' + '0'*len(s)
            order //= 2
            for additional_len in range(0, order+1):
                half_len = len(s)//2 + additional_len
                for x in range(int('1'+'0'*(half_len-1)), int('9'*half_len)+1):
                    test_id = x*10**half_len + x
                    if test_id >= lower and test_id < upper:
                        part_a += test_id
                    else:
                        continue


    print(f'{part_a = }')


    # regex brute force soln
    pat = re.compile(r'^(\d+)\1+$')

    for (s, e) in ranges:
        lower = int(s)
        upper = int(e)
        for i in range(lower, upper+1):
            if re.match(pat, str(i)):
                part_b += i

    print(f'{part_b = }')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    args = parser.parse_args()

    main(args)
