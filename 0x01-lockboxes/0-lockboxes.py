#!/usr/bin/python3
"""
0-lockboxes.py

This module contains the canUnlockAll function which determines
whether all boxes in a list of locked boxes can be opened
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened

    Args:
        boxes (list of list of int)

    Returns:
        bool: True if all boxes can be opened, False otherwise
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    visited = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if isinstance(key, int) and 0 <= key < n and key not in visited:
                visited.add(key)
                stack.append(key)

    return len(visited) == n