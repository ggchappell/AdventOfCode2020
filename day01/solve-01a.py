#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import itertools    # .combinations


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# (NONE)


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

dataset = []
for line in sys.stdin:
    line = line.rstrip()
    value = int(line)
    dataset.append(value)

# *** Do Computation ***

for v1, v2 in itertools.combinations(dataset, 2):
    if v1 + v2 == 2020:
        result = (v1, v2)
        break

# *** Print Answer ***

print(f"Answer: {v1} * {v2} = {v1*v2}")

