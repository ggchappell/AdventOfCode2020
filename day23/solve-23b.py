#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# Data Structure: list of ints: Item at index i represents cup (i+1).
# Its value is the index of the next cup clockwise. So the list of nodes
# forms a circular linked list.


# print_data - print cups in clockwise order, no delimiters, ending with
# a blank line. Begin with cup at start_index. print_start_flag is a
# bool indicating whether the cup at start_index should be printed; the
# rest are always printed.
# THIS FUNCTION IS NOT CALLED, but it is useful for debugging.
def print_data(data, start_index, print_start_flag):
    assert isinstance(data, list)
    size = len(data)
    i = start_index
    for _ in range(size):
        if print_start_flag or i != start_index:
            print(i+1, end="")
        i = data[i]
    print()


# do_move - do a single move of the game. "data" is modified.
# Return value is the new curr_index.
def do_move(data, curr_index):
    assert isinstance(cups, list)
    assert len(cups) >= 4
    # Remove & save 3 cups clockwise of current
    saved_indices = []
    i = curr_index
    for _ in range(3):
        i = data[i]
        saved_indices.append(i)
    i = data[i]
    data[curr_index] = i
    # Find destination cup and its index
    dest_index = curr_index
    while True:
        dest_index = (dest_index-1) % len(data)
        if dest_index not in saved_indices:
            break
    # Insert saved cups just after destination
    after_dest = data[dest_index]
    data[dest_index] = saved_indices[0]
    data[saved_indices[2]] = after_dest
    # Return index of new current cup
    return data[curr_index]


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

size = 1000000
assert size >= 4

cups = []
first = True
for line in sys.stdin:
    if first:
        first = False
    else:
        assert False, "More than one line in input"
    line = line.rstrip()
    for c in line:
        n = int(c)
        cups.append(n)

# Assume consecutive values
cups_sorted = cups[:]
cups_sorted.sort()
check = [ i+1 for i in range(len(cups)) ]
assert cups_sorted == check

# Make data structure
data = [None] * size
for i, c in enumerate(cups):
    data[(c-1) % size] = cups[(i+1) % len(cups)]-1
curr_index = cups[0]-1
if size > len(cups):
    data[cups[-1]-1] = len(cups)
    for i in range(len(cups), size):
        data[i] = (i+1) % size
data[-1] = curr_index

# *** Do Computation ***

num_moves = 10000000
for i in range(num_moves):
    if i % 100000 == 0:
        print(f"*** {i}")
    curr_index = do_move(data, curr_index)

# *** Print Answer ***

c1_index = data[0]
c2_index = data[c1_index]
print("-" * 60)
print(f"Answer: {(1+c1_index) * (1+c2_index)}")

