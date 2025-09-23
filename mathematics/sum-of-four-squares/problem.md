# Sum of Four Squares

- **Task**
- **Statistics**
- **Time limit:** 1.00 s
- **Memory limit:** 512 MB

A well-known result in number theory is that every non-negative integer can be represented as the sum of four squares of non-negative integers.

You are given a non-negative integer `n`. Your task is to find four non-negative integers `a`, `b`, `c`, and `d` such that: n = a² + b² + c² + d²

---

## Input

- The first line has an integer `t`: the number of test cases.
- Each of the next `t` lines has an integer `n`.

## Output

For each test case, print four non-negative integers `a`, `b`, `c`, and `d` that satisfy: n = a² + b² + c² + d²

---

## Constraints

- `1 ≤ t ≤ 1000`
- `0 ≤ n ≤ 10^7`
- The sum of all `n` is at most `10^7`

---

## Example

**Input:**
3
5
30
322266

**Output:**

2 1 0 0
1 2 3 4
314 159 265 358
