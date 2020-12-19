#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import re           # .search


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def lex(ss):
    tokens = []
    while ss:
        mo1 = re.search(r"^(\d+)(.*)$", ss)
        if mo1:  # Number
            num = int(mo1[1])
            tokens.append(num)
            ss = mo1[2]
        else:    # Blank (skipped) or 1-character token
            c = ss[0]
            if c != " ":
                tokens.append(c)
            ss = ss[1:]
    return tokens


# Recursive-descent evaluator based on the following grammar:
# expr     -> plusexpr { '*' plusexpr }
# plusexpr -> num { '+' num }
# num      -> INTEGER | '(' expr ')'


def eval_expr(tokens):
    val = eval_plusexpr(tokens)
    while tokens and tokens[0] == "*":
        op = tokens[0]
        tokens.pop(0)
        val2 = eval_plusexpr(tokens)
        val *= val2
    return val


def eval_plusexpr(tokens):
    val = eval_num(tokens)
    while tokens and tokens[0] == "+":
        op = tokens[0]
        tokens.pop(0)
        val2 = eval_num(tokens)
        val += val2
    return val


def eval_num(tokens):
    if isinstance(tokens[0], int):
        val = tokens[0]
        tokens.pop(0)
    elif tokens[0] == "(":
        tokens.pop(0)
        val = eval_expr(tokens)
        assert tokens and tokens[0] == ")"
        tokens.pop(0)
    else:
        assert False
    return val


def eval(orig_tokens):
    assert isinstance(orig_tokens, list)
    assert orig_tokens
    tokens = orig_tokens[:]
    return eval_expr(tokens)


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

expressions = []
for line in sys.stdin:
    line = line.rstrip()
    tokens = lex(line)
    expressions.append(tokens)

# *** Do Computation ***

result = 0
for tokens in expressions:
    value = eval(tokens)
    result += value

# *** Print Answer ***

print(f"Answer: {result}")

