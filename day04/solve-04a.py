#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def is_record_valid(record):
    set1 = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" }
    set2 = set1.copy()
    set2.add("cid")

    ks = set(record.keys())
    return ks == set1 or ks == set2


def get_record(record_str):
    record = {}
    for f in record_str.split():
        [k, v] = f.split(":")
        record[k] = v
    return record


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

records = []
record_str = ""
for line in sys.stdin:
    line = line.rstrip()
    if line:
        record_str += " " + line
        continue
    records.append(get_record(record_str))
    record_str = ""  # Prep for next
if record_str:
    records.append(get_record(record_str))

# *** Do Computation ***

valid_count = 0
for record in records:
    if is_record_valid(record):
        valid_count += 1

# *** Print Answer ***

print(f"Answer: {valid_count}")

