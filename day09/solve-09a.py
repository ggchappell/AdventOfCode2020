#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin, .argv
import itertools    # .combinations


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def is_sum(val, the_list):
    for a, b in itertools.combinations(the_list, 2):
        if val == a + b:
            return True
    return False


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

# Optional command-line argument tells how many previous numbers to
# consider (default: 25)
how_many_previous = 25
if len(sys.argv) > 1:
    how_many_previous = int(sys.argv[1])

num_list = []
for line in sys.stdin:
    line = line.rstrip()
    num_list.append(int(line))

# *** Do Computation ***

for i, v in enumerate(num_list):
    if i < how_many_previous:
        continue
    if not is_sum(v, num_list[i-how_many_previous:i]):
        result = v
        break

# *** Print Answer ***

print(f"Answer: {result}")

