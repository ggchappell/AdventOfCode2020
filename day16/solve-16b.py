#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import re           # .search
#import itertools    # .count, .combinations, .permutations, .chain
#import copy         # .deepcopy
#import collections  # .defaultdict
#import os           # .system
#import time         # .sleep


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def does_rule_allow_num(rule, num):
    assert isinstance(rule, list)
    assert len(rule) == 5
    assert isinstance(rule[0], str)
    for k in rule[1:]:
        assert isinstance(k, int)
    assert rule[1] <= rule[2]
    assert rule[3] <= rule[4]
    assert isinstance(num, int)

    return rule[1] <= num <= rule[2] or rule[3] <= num <= rule[4]


# check_valid_ticket - returns list of all invalid numbers found in the
# given ticket, according to the given rules. For a valid ticket, this
# list will be empty.
def check_valid_ticket(rules, ticket):
    assert isinstance(rules, list)
    assert isinstance(ticket, list)

    invalid_numbers = []
    for n in ticket:
        for r in rules:
            if does_rule_allow_num(r, n):
                break
        else:
            invalid_numbers.append(n)
    return invalid_numbers


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

# Read rules
rules = []
for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    re1 = r"^([a-z][a-z ]*[a-z]|[a-z]): (\d+)-(\d+) or (\d+)-(\d+)$"
    mo1 = re.search(re1, line)
    assert mo1
    the_rule = [mo1[1],
                int(mo1[2]), int(mo1[3]), int(mo1[4]), int(mo1[5])]
    rules.append(the_rule)
rules_count = len(rules)

# Read your ticket
line = sys.stdin.readline()
line = line.rstrip()
assert line == "your ticket:"
line = sys.stdin.readline()
line = line.rstrip()
ticket_strs = line.split(",")
your_ticket = [ int(n_str) for n_str in ticket_strs ]
assert len(your_ticket) == rules_count
line = sys.stdin.readline()
line = line.rstrip()
assert line == ""

# Read nearby tickets
line = sys.stdin.readline()
line = line.rstrip()
assert line == "nearby tickets:"
nearby_tickets = []
for line in sys.stdin:
    line = line.rstrip()
    assert line != ""
    ticket_strs = line.split(",")
    the_ticket = [ int(n_str) for n_str in ticket_strs ]
    assert len(the_ticket) == rules_count
    nearby_tickets.append(the_ticket)

# *** Do Computation ***

# Get list of valid nearby tickets
valid_nearby_tickets = []
for nt in nearby_tickets:
    invalid_numbers = check_valid_ticket(rules, nt)
    if not invalid_numbers:
        valid_nearby_tickets.append(nt)

# Find allowed rules for each position
all_rule_nums = set(range(rules_count))
allowed_rule_nums_list = []
for pi in range(rules_count):      # Position in ticket
    disallowed_rule_nums = set()
    for ri in range(rules_count):  # Rule no.
        for nt in valid_nearby_tickets:
            if not does_rule_allow_num(rules[ri], nt[pi]):
                disallowed_rule_nums.add(ri)
                break
    allowed_rule_nums_list.append(all_rule_nums - disallowed_rule_nums)

# Compute which rule each position matches with, using AND MODIFYING
# allowed_rule_nums_list
which_rule_list = [None] * rules_count
positions_matched_count = 0
while positions_matched_count < rules_count:
    for pi in range(rules_count):
        if len(allowed_rule_nums_list[pi]) == 1:
            break
    else:
        assert False, "No list of allowed rule no's of length 1 found"
    assert which_rule_list[pi] is None
    the_rule_num = allowed_rule_nums_list[pi].pop()
    which_rule_list[pi] = the_rule_num
    for pi2 in range(rules_count):
        allowed_rule_nums_list[pi2] -= {the_rule_num}
    positions_matched_count += 1

# *** Print Answer ***

product = 1
print("Your Ticket:")
for pi in range(rules_count):
    ri = which_rule_list[pi]
    rule_name = rules[ri][0]
    if re.search(r"departure", rule_name):
        print("* ", end="")
        product *= your_ticket[pi]
    else:
        print("  ", end="")
    print(f"{rule_name}: {your_ticket[pi]}")
print("-" * 60)
print(f"Answer: {product}")

