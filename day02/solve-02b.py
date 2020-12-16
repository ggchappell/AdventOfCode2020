#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def is_valid(info):
    pos1 = info[0]-1
    pos2 = info[1]-1
    char = info[2]
    pwd = info[3]
    assert 0 <= pos1 < len(pwd)
    assert 0 <= pos2 < len(pwd)

    got1 = pwd[pos1] == char
    got2 = pwd[pos2] == char
    return (got1 and not got2) or (got2 and not got1)


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

dataset = []
for line in sys.stdin:
    fields = line.split()
    assert len(fields) == 3
    limits = fields[0].split("-")
    assert len(limits) == 2
    dataset.append([int(limits[0]), int(limits[1]), fields[1][0],
                   fields[2]])

# *** Do Computation ***

valid_count = 0
for item in dataset:
    if is_valid(item):
        valid_count += 1

# *** Print Answer ***

print(f"Answer: {valid_count}")

