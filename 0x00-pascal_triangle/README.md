# 0x00. Pascal's Triangle

##  Directory: `0x00-pascal_triangle`  
> Part of the **ALX Interview Prep** Series

---

##  Project Description

This project focuses on generating **Pascal's Triangle** using **Python**. You will write a function that builds a triangle of `n` rows, represented as a list of lists, applying core algorithmic and programming skills.

---

##  Learning Objectives

To successfully complete this project, you should have a solid understanding of the following Python concepts:

- **Lists and List Comprehensions**
- **Functions & Parameters**
- **Loops (for, while, nested)**
- **Conditional Statements**
- **Arithmetic Operations**
- **Indexing and Slicing**
- (Optional) **Recursion**
- (Optional) **Error and Exception Handling**
- **Efficiency and Optimization**

---

##  Background

**Pascal’s Triangle** is a triangular array where each number is the sum of the two numbers directly above it. It begins as follows:

  [1]
 [1,1]
[1,2,1]

[1,3,3,1] [1,4,6,4,1] ...

More info:
- [Pascal's Triangle - Wikipedia](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
- [Numberphile Video on Pascal’s Triangle](https://www.youtube.com/watch?v=0iMtlus-afo)

---

## 🧪 Requirements

- Python 3.x
- Code must follow **PEP8** style
- Function must be contained in `0-pascal_triangle.py`
- Must pass provided test cases

---

## ✅ Task

### `0. Pascal's Triangle`

Create a function:

```python
def pascal_triangle(n):

Requirements:
Returns a list of lists of integers representing the Pascal’s triangle of n

Returns an empty list if n <= 0

Assumes n is always an integer