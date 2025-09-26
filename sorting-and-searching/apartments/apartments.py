def apartments(
    n_applicants: int,
    n_apartments: int,
    k: int,
    desired_size: list[int],
    available_size: list[int],
) -> None:

    if not (1 <= n_applicants <= 200_000):
        print("Number of applicants must be between 1 and 200000")
        return
    if not (1 <= n_apartments <= 200_000):
        print("Number of apartments must be between 1 and 200000")
        return
    if not (0 <= k <= 1_000_000_000):
        print("Maximum allowed difference must be between 0 and 1e9")
        return
    if len(desired_size) != n_applicants:
        print("Length of desired_size list must match n_applicants")
        return
    if len(available_size) != n_apartments:
        print("Length of available_size list must match n_apartments")
        return

    for idx, size in enumerate(desired_size):
        if not (1 <= size <= 1_000_000_000):
            print(f"desired_size[{idx}] must be between 1 and 1e9")
            return

    for idx, size in enumerate(available_size):
        if not (1 <= size <= 1_000_000_000):
            print(f"available_size[{idx}] must be between 1 and 1e9")
            return

    desired_size.sort()
    available_size.sort()

    i = j = 0
    success = 0

    while i < n_applicants and j < n_apartments:
        if abs(desired_size[i] - available_size[j]) <= k:
            success += 1
            i += 1
            j += 1
        elif available_size[j] < desired_size[i] - k:
            j += 1
        else:
            i += 1

    print(success)


apartments(4, 3, 5, [60, 45, 80, 60], [30, 60, 75])
