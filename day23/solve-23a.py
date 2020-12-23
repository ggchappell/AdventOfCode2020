#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# do_move - do a single move of the game. "cups" is modified.
# cups is a list of cup numbers in clockwise order, with the current cup
# in the first spot. cups is modified so that all this will be true for
# the next move as well.
def do_move(cups):
    assert isinstance(cups, list)
    assert len(cups) >= 4
    # Find & save max value in cups list
    max_cup = max(cups)
    # Remove & save 3 cups clockwise of current
    saved = []
    for _ in range(3):
        c = cups.pop(1)
        saved.append(c)
    # Find destination cup and its index
    dest_cup = cups[0]
    while True:
        dest_cup -= 1
        if dest_cup == 0:
           dest_cup = max_cup
        if dest_cup in cups:
            break
    try:
        dest_index = cups.index(dest_cup)
    except:
        assert False
    # Insert saved cups just after destination
    for i in range(3):
        c = saved.pop(0)
        cups.insert(dest_index + i + 1, c)
    # Rotate cups list so new current cup is at the beginning
    cc = cups.pop(0)
    cups.append(cc)


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

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

# *** Do Computation ***

num_moves = 100
for _ in range(num_moves):
    do_move(cups)

# *** Print Answer ***

try:
    i = cups.index(1)
except:
    assert False
print("Answer: ", end="")
for k in range(i+1, i+len(cups)):
    print(cups[k % len(cups)], end="")
print()

