#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import re           # .search


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
assert not line

# Read nearby tickets
line = sys.stdin.readline()
line = line.rstrip()
assert line == "nearby tickets:"
nearby_tickets = []
for line in sys.stdin:
    line = line.rstrip()
    assert line
    ticket_strs = line.split(",")
    the_ticket = [ int(n_str) for n_str in ticket_strs ]
    assert len(the_ticket) == rules_count
    nearby_tickets.append(the_ticket)

# *** Do Computation ***

all_invalid_numbers = []
for nt in nearby_tickets:
    invalid_numbers = check_valid_ticket(rules, nt)
    all_invalid_numbers += invalid_numbers

# *** Print Answer ***

print(f"Answer: {sum(all_invalid_numbers)}")

