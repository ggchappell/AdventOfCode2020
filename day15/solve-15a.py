#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def generate_numbers(start_list):
    assert isinstance(start_list, list)
    assert len(start_list) > 0
    number_list = []
    while True:
        n = len(number_list)
        if n < len(start_list):
            new_num = start_list[n]
        else:
            last_num = number_list[-1]
            for k in range(n-2, -1, -1):
                if number_list[k] == last_num:
                    new_num = (n-1)-k
                    break
            else:
                new_num = 0
        number_list.append(new_num)
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

index_of_value = 2020
for i, num in enumerate(generate_numbers(start_list)):
    if i+1 == index_of_value:
        result = num
        break

# *** Print Answer ***

print(f"Answer: {result}")

