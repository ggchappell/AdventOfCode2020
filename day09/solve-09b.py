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


def compute_soln(the_list, i, k):
    sublist = the_list[i:k+1]
    return min(sublist) + max(sublist)


def find_soln(the_list, val):
    for i in range(len(the_list)):
        total = the_list[i]
        for k in range(i+1, len(the_list)):
            total += the_list[k]
            if total == val:
                return compute_soln(num_list, i, k)
            elif total > val:
                break


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
        break
result = find_soln(num_list, v)

# *** Print Answer ***

print(f"Answer: {result}")

