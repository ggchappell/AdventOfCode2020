#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import re           # .search


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


def matches(rules, rnum, s):
    success, rest = match_part(rules, rnum, s)
    return success and not rest


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

# *** Do Computation ***

match_count = 0
for s in strings:
    if matches(rules, 0, s):
        match_count += 1

# *** Print Answer ***

print(f"Answer: {match_count}")

