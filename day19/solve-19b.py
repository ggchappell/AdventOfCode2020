#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import re           # .search
import itertools    # .product
import copy         # .deepcopy


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# match_part: returns (True, rest_of_s) if beginning of s matches rule,
# (False, ???) otherwise. We go with the first way to match that is
# found.
def match_part(rules, rnum, s):
    r = rules[rnum]
    if isinstance(r, str):
        if not s or s[0] != r:
            return (False, None)
        return (True, s[1:])
    assert isinstance(r, list)
    for rr in r:
        assert isinstance(rr, list)
        ss = s[:]
        for rnum2 in rr:
            assert isinstance(rnum2, int)
            success, rest = match_part(rules, rnum2, ss)
            if not success:
                break
            ss = rest
        else:
            return (True, ss)
    return (False, None)


def matches(orig_rules, rnum, s):
    if not update_rules_8_11:
        success, rest = match_part(orig_rules, rnum, s)
        return success and not rest
    max_depth = 5  # This is all we need, for the inputs given
    for d8, d11 in itertools.product(range(max_depth), repeat=2):
        rules = copy.deepcopy(orig_rules)
        rules[8] = [[42]*(1+d8)]
        rules[11] = [[42]*(1+d11) + [31]*(1+d11)]
        success, rest = match_part(rules, rnum, s)
        if success and not rest:
            return True
    return False


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

rules = {}
for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    mo1 = re.search(r"^(\d+): (.*)$", line)
    assert mo1
    rule_num = int(mo1[1])
    rule_body_str = mo1[2]
    assert rule_body_str
    if rule_body_str[0] == '"':
        assert len(rule_body_str) >= 3
        rule_body = rule_body_str[1]
    else:
        rule_body_tokens = rule_body_str.split()
        rule_body = []
        rule_body_part = []
        for t in rule_body_tokens:
            if t == "|":
                rule_body.append(rule_body_part)
                rule_body_part = []
            else:
                rule_body_part.append(int(t))
        rule_body.append(rule_body_part)
    rules[rule_num] = rule_body
assert rules

strings = []
for line in sys.stdin:
    line = line.rstrip()
    strings.append(line)

# Do special rule changes for part 2?
update_rules_8_11 = False
if 8 in rules and 11 in rules:
    update_rules_8_11 = rules[8] == [[42]] and rules[11] == [[42, 31]]

# *** Do Computation ***

match_count = 0
for s in strings:
    if matches(rules, 0, s):
        match_count += 1

# *** Print Answer ***

print(f"Answer: {match_count}")

