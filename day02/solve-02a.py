#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def is_valid(info):
    min_c = info[0]
    max_c = info[1]
    char = info[2]
    pwd = info[3]

    count = 0
    for c in pwd:
        if c == char:
            count += 1
    return min_c <= count <= max_c


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

