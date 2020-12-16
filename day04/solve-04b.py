#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def is_k_digit(the_str, k=None):
    assert isinstance(the_str, str)
    if k is None:
        k = len(the_str)
    assert isinstance(k, int)

    if len(the_str) != k:
        return False
    for c in the_str:
        if c < "0" or c > "9":
            return False
    return True


def is_hex_num(the_str):
    for c in the_str:
        if (c < "0" or c > "9") and (c < "a" or c > "f"):
            return False
    return True


def is_field_valid(key, val):
    if key == "byr":
        return is_k_digit(val, 4) and 1920 <= int(val) <= 2002
    elif key == "iyr":
        return is_k_digit(val, 4) and 2010 <= int(val) <= 2020
    elif key == "eyr":
        return is_k_digit(val, 4) and 2020 <= int(val) <= 2030
    elif key == "hgt":
        if len(val) < 3:
            return False
        unit = val[-2:]
        if unit != "cm" and unit != "in":
            return False
        num = val[:-2]
        if len(num) == 0 or not is_k_digit(num):
            return False
        num_value = int(num)
        if unit == "cm":
            return 150 <= num_value <= 193
        elif unit == "in":
            return 59 <= num_value <= 76
        else:
            assert False
    elif key == "hcl":
        if len(val) != 7:
            return False
        if val[0] != "#":
            return False
        return is_hex_num(val[1:])
    elif key == "ecl":
        return val in { "amb", "blu", "brn", "gry", "grn", "hzl",
                        "oth" }
    elif key == "pid":
        return is_k_digit(val, 9)
    elif key == "cid":
        return True
    else:
        return False


def is_record_valid(record):
    set1 = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" }
    set2 = set1.copy()
    set2.add("cid")

    ks = set(record.keys())
    if ks != set1 and ks != set2:
        return False
    for key in record:
        val = record[key]
        if not is_field_valid(key, val):
            return False
    return True


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

