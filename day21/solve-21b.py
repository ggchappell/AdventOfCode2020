#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import re           # .search
import functools    # .reduce


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
    mo1 = re.search(r"^(.*) \(contains (.*)\)$", line)
    assert mo1
    ingredients_str = mo1[1]
    allergens_str = mo1[2]
    ingredients_list = ingredients_str.split()
    allergens_list = allergens_str.split(", ")
    dataset.append([set(ingredients_list), set(allergens_list)])
for ll in dataset:
    for ss in ll:
        for item in ss:
            assert re.search(r"^[a-z]+$", item)

# *** Do Computation ***

# Make set of all allergens.
all_allergens = set()
for ll in dataset:
    all_allergens |= ll[1]

# For each listed allergen, find ingredients that MIGHT contain it.
# Put these in a dict, with the allergen as the key.
may_contain = {}
for allergen in all_allergens:
    intersection = functools.reduce(
        lambda a,b: a & b,  # set intersection
        ( ll[0] for ll in dataset if allergen in ll[1] ))
    # Above raises exception if there is no ll with allergen in ll[1].
    # So we are effectively asserting that.
    may_contain[allergen] = intersection

# Make list of pairs: allergen and THE ingredient containing it.
# may_contain is modified
contains = []
while may_contain:
    for aa in may_contain:
        if len(may_contain[aa]) == 1:
            break
    else:
        assert False, "No set of ingredients of length 1 found"
    ii = may_contain[aa].pop()
    del may_contain[aa]
    for aa2 in may_contain:
        may_contain[aa2] -= {ii}
    contains.append((aa, ii))

# Sort list by allergen
contains.sort()

# *** Print Answer ***

result = ""
for _, ii in contains:
    if result:
        result += ","
    result += ii
print(f"Answer: {result}")

