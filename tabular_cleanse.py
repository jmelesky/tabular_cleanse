#!/usr/bin/env python -tt
# I use -tt, just to make a point.

# According to the python language definition,
#
#    First, tabs are replaced (from left to right) by one to eight
#    spaces such that the total number of characters up to and
#    including the replacement is a multiple of eight (this is
#    intended to be the same rule as used by Unix).
#
# (source: http://docs.python.org/reference/lexical_analysis.html#indentation )

import sys
import math


def next_multiple_of(factor, num):
    """
    Returns the next multiple of 'factor' that is greater than 'num'.

    >>> next_multiple_of(4, 5)
    8
    >>> next_multiple_of(4, 8)
    8
    >>> next_multiple_of(12, 77)
    84
    """
    return factor * (int(math.floor(float(num) / factor)) + 1)


def canonicalize_tabs(line):
    indenting_spaces = 0
    for x in line:
        if x == ' ':
            indenting_spaces += 1
        elif x == "\t":
            indenting_spaces = next_multiple_of(8, indenting_spaces)
        else:
            # past preceding whitespace, so we're done
            break
    # TOTHINK: should i have an "else" block in case it's all whitespace?

    indentation = ' ' * indenting_spaces
    return indentation + line.lstrip()

def main():
    for line in sys.stdin:
        print canonicalize_tabs(line),

if __name__ == '__main__':
    main()
