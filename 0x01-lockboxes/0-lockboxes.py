#!/usr/bin/python3
"""Number of locked boxes in front of you
Each box is numbered sequentially
from 0 to n  - 1"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
