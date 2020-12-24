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

# Make sets of all ingredients and all allergens.
all_ingredients = set()
all_allergens = set()
for ll in dataset:
    all_ingredients |= ll[0]
    all_allergens |= ll[1]

# For each listed allergen, find ingredients that MIGHT contain it.
# Make a set of all of these maybe-ingredients.
maybe_ingredients = set()
for allergen in all_allergens:
    intersection = functools.reduce(
        lambda a,b: a & b,
        ( ll[0] for ll in dataset if allergen in ll[1] )
        )
    # Above raises exception if there is no ll with allergen in ll[1].
    # So we are effectively asserting that.
    maybe_ingredients |= intersection

# Find ingredients that cannot possibly contains any listed allergens.
cannot_ingredients = all_ingredients - maybe_ingredients

# *** Print Answer ***

cannot_count = 0
for ii in cannot_ingredients:
    for ll in dataset:
        if ii in ll[0]:
            cannot_count += 1
print(f"Answer: {cannot_count}")

