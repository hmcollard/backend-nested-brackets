#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Nested Brackets: Determine if a line of code has properly nested brackets.
"""
__author__ = "Haley Collard"

import sys


def is_nested(line):
    """Validate a single input line for correct nesting"""
    opening_brackets = ['(', '[', '{', '<', '(*']
    closing_brackets = ['*)', '>', '}', ']', ')']
    brackets = []
    for char in line:
        if char in opening_brackets:
            brackets.append(char)
        elif char in closing_brackets:
            if not brackets:
                return 'NO'
            else:
                brackets.pop()
    if not brackets:
        return 'YES'
    else:
        return 'NO'


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    results = []
    with open('input.txt', 'r') as f:
        text = f.readlines()
        for line in text:
            result = is_nested(line)
            results.append(result)

    print(results)
    with open("output.txt", 'w') as f:
        f.write(results)


if __name__ == '__main__':
    main(sys.argv[1:])
