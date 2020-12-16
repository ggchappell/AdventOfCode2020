#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def to_set(line):
    s = set()
    for c in line:
        s.add(c)
    return s


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

group_lines = []
the_sets = []
for line in sys.stdin:
    line = line.rstrip()
    if line != "":
        s = to_set(line)
        the_sets.append(s)
        continue
    group_lines.append(the_sets)
    the_sets = []
if the_sets != []:
    group_lines.append(the_sets)

# *** Do Computation ***

total = 0
for set_list in group_lines:
    assert len(set_list) > 0
    s = set_list[0]
    for ss in set_list[1:]:
        s &= ss
    total += len(s)

# *** Print Answer ***

print(f"Answer: {total}")

