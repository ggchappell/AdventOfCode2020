#!/usr/bin/env python3
# Advent of Code 2020
# Glenn G. Chappell

import sys          # .stdin
import re           # .search


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# A deck is a list in top-to-bottom order.

# round - Play one round of Recursive Combat. Given decks are modified.
# Infinite game prevention rule not enforced for this game.
def round(deck1, deck2):
    assert isinstance(deck1, list)
    assert isinstance(deck2, list)
    assert deck1 and deck2
    c1 = deck1.pop(0)
    c2 = deck2.pop(0)
    if c1 <= len(deck1) and c2 <= len(deck2):
        winner = game(deck1[:c1], deck2[:c2])
    else:
        assert c1 != c2, "Decks contain identical card"
        if c1 > c2:
            winner = 1
        else:
            winner = 2
    if winner == 1:
        deck1.append(c1)
        deck1.append(c2)
    else:
        deck2.append(c2)
        deck2.append(c1)


# game - Play a game of Recursive Combat. Given decks are modified.
# Return value is number of winning player: 1 or 2.
def game(deck1, deck2):
    assert isinstance(deck1, list)
    assert isinstance(deck2, list)
    saved = set()  # Saved games: (tuple(deck1), tuple(deck2))
    while deck1 and deck2:
        key = (tuple(deck1), tuple(deck2))
        if key in saved:
            return 1
        saved.add(key)
        round(deck1, deck2)
    assert deck1 or deck2
    if not deck1:
        return 2
    elif not deck2:
        return 1
    else:
        assert False
    

# score - Given deck, in top-to-bottom order, return score.
def score(deck):
    assert isinstance(deck, list)
    assert deck
    size = len(deck)
    score = 0
    for i, c in enumerate(deck):
        score += (size-i)*c
    return score


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

deck1 = []
deck2 = []
reading = 0  # Which deck to read; 0: none specified yet
for line in sys.stdin:
    line = line.rstrip()
    if line == "Player 1:":
        reading = 1
        assert not deck1
    elif line == "Player 2:":
        reading = 2
        assert not deck2
    elif not line:
        reading = 0
    else:
        assert re.search(r"^\d+$", line)
        card = int(line)
        if reading == 1:
            deck1.append(card)  # Want decks top-to-bottom
        elif reading == 2:
            deck2.append(card)
        else:
            assert False, "Got card before deck specified"

# *** Do Computation ***

# Play the game until a player wins
winner = game(deck1, deck2)

# *** Print Answer ***

# Find winning player's score
if winner == 1:
    print("Player 1 wins")
    result = score(deck1)
elif winner == 2:
    print("Player 2 wins")
    result = score(deck2)
else:
    assert False
print(f"Answer: {result}")

