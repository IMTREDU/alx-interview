# 0x01. Lockboxes

## Description

This project is part of the **ALX Interview Preparation** curriculum. The task is to write an algorithm that determines if all the boxes in a list can be unlocked. Each box may contain keys to other boxes.

---

## Learning Objectives

To successfully complete this project, you should understand the following concepts:

- **Lists and List Manipulation**
- **Graph Theory Basics** (e.g., Depth-First Search or Breadth-First Search)
- **Algorithmic Complexity** (Big O Notation)
- **Recursion**
- **Queue and Stack**
- **Set Operations**

These concepts help you design an efficient traversal through boxes and keys, similar to navigating a graph structure.

---

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.4.3**
- All files must end with a new line
- The first line of all files should be: `#!/usr/bin/python3`
- Code should follow **PEP 8** style (version 1.7.x)
- All files must be executable
- You must have a `README.md` at the root of your project
- Code must be documented

---

## Prototype

```python
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): Each box contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """