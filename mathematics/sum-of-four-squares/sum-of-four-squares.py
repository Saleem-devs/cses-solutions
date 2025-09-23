import math
from typing import List, Optional


def find_perfect_square(num: int) -> Optional[int]:
    sqrt = math.isqrt(num)
    return sqrt if sqrt * sqrt == num else None


def find_three_squares(num: int) -> Optional[List[int]]:
    m = num
    while m % 4 == 0:
        m //= 4
    if m % 8 == 7:
        return None

    for a in range(int(math.isqrt(num)) + 1):
        for b in range(int(math.isqrt(num - a * a)) + 1):
            c2 = num - a * a - b * b
            if c2 >= 0:
                c = math.isqrt(c2)
                if c * c == c2:
                    return [a, b, c]
    return None


def sum_of_four_squares(input: List[int]):
    num_of_test_cases = input[0]
    n_values = input[1:]

    if num_of_test_cases < 1 or num_of_test_cases > 1000:
        print("The number of test cases must be at least 1 and at most 1000")
        return

    if num_of_test_cases != len(n_values):
        print("The num_of_test_cases must equal the available test cases")

    for n in n_values:
        if n == 0:
            print("0 0 0 0")
            continue

        sqrt = find_perfect_square(n)
        if sqrt is not None:
            print(f"{sqrt} 0 0 0")
            continue

        for a in range(int(math.isqrt(n)), -1, -1):
            r = n - a * a
            three_squares = find_three_squares(r)
            if three_squares:
                print(f"{three_squares[0]} {three_squares[1]} {three_squares[2]} {a}")
                break


sum_of_four_squares([5, 5, 30, 74, 17, 322266])
