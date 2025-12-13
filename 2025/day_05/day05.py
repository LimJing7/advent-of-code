# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 2025 8:00:43 PM

@author: Lim Jing
"""

import argparse
def main(args):
    ranges : list[tuple[int, int]] = []
    ingredients = set()
    range_phase = True
    with open(args.input_file) as f:
        for line in f:
            line = line.strip()
            if line == '':
                range_phase = False
                continue
            if range_phase:
                a, b = map(int, line.split('-'))
                to_fix = set()
                action = ''
                for range_idx, (start, end) in enumerate(ranges):
                    if a >= start and b <= end:
                        action = 'skip'
                        break
                    if a >= start and a <= end and b >= end:
                        action = 'fix'
                        to_fix.add(range_idx)
                    if a <= start and b >= start and b <= end:
                        action = 'fix'
                        to_fix.add(range_idx)
                    if a <= start and b >= end:
                        action = 'fix'
                        to_fix.add(range_idx)
                else:
                    if action == 'fix':
                        combined = (a, b)
                        for range_idx in to_fix:
                            (start, end) = ranges[range_idx]
                            if combined[0] >= start and combined[0] <= end and combined[1] >= end:
                                combined = (start, combined[1])
                            elif combined[0] <= start and combined[1] >= start and combined[1] <= end:
                                combined = (combined[0], end)
                            elif start >= combined[0] and end <= combined[1]:
                                pass
                            else:
                                raise ValueError
                        for range_idx in sorted(to_fix, reverse=True):
                            ranges.pop(range_idx)
                        ranges.append(combined)
                    else:
                        ranges.append((a, b))
            else:
                ingredients.add(int(line))

    part_a = 0
    for ingredient in ingredients:
        for (start, end) in ranges:
            if ingredient >= start and ingredient <= end:
                part_a += 1
                break

    print(f'{part_a = }')

    part_b = 0
    for (start, end) in ranges:
        part_b += (end - start + 1)

    print(f'{part_b = }')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    args = parser.parse_args()

    main(args)
