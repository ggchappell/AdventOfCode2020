#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import itertools    # .count


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def generate_numbers(start_list):
    assert isinstance(start_list, list)
    assert len(start_list) > 0
    number_dict = {}
    for n in itertools.count(0):
        if n < len(start_list):
            new_num = start_list[n]
        else:
            new_num = next_num
        if new_num in number_dict:
            next_num = n-number_dict[new_num]
        else:
            next_num = 0
        number_dict[new_num] = n
        yield new_num


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

line = sys.stdin.readline()
line = line.rstrip()
num_strs = line.split(",")
start_list = [ int(s) for s in num_strs ]

# *** Do Computation ***

index_of_value = 30000000
for i, num in enumerate(generate_numbers(start_list)):
    if (i+1) <= 20 or (i+1) % 100000 == 0:
        print(i+1, num)
    if i+1 == index_of_value:
        result = num
        break

# *** Print Answer ***

print("-" * 60)
print(f"Answer: {result}")

