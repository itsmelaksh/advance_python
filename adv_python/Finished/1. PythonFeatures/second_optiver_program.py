def calculateFastestKilometreSpeed(distances: List[int]) -> float:
    """
    distances: list[int]
        Each element is the distance (in metres) covered in a 5-second interval.
    Returns: float
        Fastest average speed (m/s) over 1 km. Returns 0 if < 1000m total.
    """
    # type checks
    if not isinstance(distances, list):
        raise TypeError("distances must be a list of integers")
    if not all(isinstance(d, int) and d >= 0 for d in distances):
        raise TypeError("all elements in distances must be non-negative integers")

    if not distances:
        return 0.0

    n = len(distances)

    # prefix sums of distances
    prefix_sums = [0]
    for d in distances:
        prefix_sums.append(prefix_sums[-1] + d)

    max_speed = 0.0

    # try each possible starting interval
    for start_idx in range(n):
        start_distance = prefix_sums[start_idx]
        target_distance = start_distance + 1000

        # find the first interval where cumulative distance >= target
        end_idx = start_idx + 1
        while end_idx <= n and prefix_sums[end_idx] < target_distance:
            end_idx += 1
        if end_idx > n:
            break  # not enough distance left

        # interpolate within the interval where we crossed 1000m
        interval_distance = distances[end_idx - 1]
        extra_distance = target_distance - prefix_sums[end_idx - 1]
        fraction = extra_distance / interval_distance if interval_distance > 0 else 0

        # compute time taken (seconds)
        time_taken = (end_idx - start_idx - 1) * 5 + fraction * 5

        if time_taken > 0:
            avg_speed = 1000.0 / time_taken
            max_speed = max(max_speed, avg_speed)

    return max_speed