#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import functools    # .reduce


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# (NONE)


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

group_lines = []
the_sets = []
for line in sys.stdin:
    line = line.rstrip()
    if line:
        the_sets.append(set(line))  # Append set of chars in line
        continue
    group_lines.append(the_sets)
    the_sets = []
if the_sets != []:
    group_lines.append(the_sets)

# *** Do Computation ***

total = 0
for set_list in group_lines:
    assert set_list
    intersection = functools.reduce(
        lambda a,b: a & b,  # set intersection
        set_list)
    total += len(intersection)

# *** Print Answer ***

print(f"Answer: {total}")

