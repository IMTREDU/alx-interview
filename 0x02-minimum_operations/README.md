# 0x02. Minimum Operations

## Description

This project focuses on algorithm design and optimization using Python. The main task is to determine the minimum number of operations required to produce exactly `n` characters `H` using only two operations: `Copy All` and `Paste`.

Given an initial file with a single character `H`, the allowed operations must be used to reach the exact number of characters specified. The goal is to minimize the number of operations.

---

## Requirements

- **Language:** Python 3.4.3
- **Editor:** `vi`, `vim`, or `emacs`
- All Python files must:
  - Have `#!/usr/bin/python3` as the first line
  - End with a new line
  - Be executable
  - Follow [PEP 8](https://pep8.org/) style guidelines (version 1.7.x)
  - Be documented

---

## Usage

To test your solution:

```bash
$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
