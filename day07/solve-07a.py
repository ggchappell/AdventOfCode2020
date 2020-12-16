#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import re           # .search


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def process_line(line):
    mo1 = re.search(r"^([^ ]+ [^ ]+) bags? contain (.*)$", line)
    assert mo1
    key = mo1[1]
    rest = mo1[2]
    assert rest[-1] == "."
    rest = rest[:-1]
    contents = {}
    if rest == "no other bags":
        return key, contents
    rest_list = rest.split(", ")
    for r in rest_list:
        assert isinstance(r, str)
        if r[-4:] == " bag":
            r = r[:-4]
        elif r[-5:] == " bags":
            r = r[:-5]
        else:
            assert False
        mo2 = re.search(r"^(\d+) ([^ ]+ [^ ]+)$", r)
        assert mo2
        count = int(mo2[1])
        other_key = mo2[2]
        contents[other_key] = count
    return key, contents


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

dataset = {}
for line in sys.stdin:
    line = line.rstrip()
    key, contents = process_line(line)
    dataset[key] = contents

# *** Do Computation ***

contained_in = {}
for key in dataset:
    for other_key in dataset[key]:
        if other_key not in contained_in:
            contained_in[other_key] = set()
        contained_in[other_key].add(key)

k = "shiny gold"
can_hold = set()
stack = []
for kk in contained_in[k]:
    stack.append(kk)
while stack:
    curr = stack.pop()
    if curr in can_hold:
        continue
    can_hold.add(curr)
    if curr in contained_in:
        for kk in contained_in[curr]:
            if kk not in can_hold:
                stack.append(kk)
result = len(can_hold)

# *** Print Answer ***

print(f"Answer: {result}")

