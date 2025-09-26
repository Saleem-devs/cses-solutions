def find_distinct_values(num_of_values: int, values: list[int]):
    if num_of_values < 1 or num_of_values > 200000:
        print("number of values must be at least 1 and not more than 200000")
        return

    if num_of_values != len(values):
        print("number of values and length of values do not match")
        return
    distinct = set()

    for index, value in enumerate(values):
        if (value < 1) or (value > 1000000000):
            print(f"x{index + 1} must be at least 1 and not more than 1000000000")
            return
        distinct.add(value)

    print(len(distinct))


find_distinct_values(5, [2, 3, 2, 2, 3])
