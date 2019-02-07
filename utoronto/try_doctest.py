def get_divisors(num, possible_divisors):
    """
    (int, list of int) -> list of int
    >>> get_divisors(8, [1,2,3])
    [1, 2]
    >>> get_divisors(4, [-2,0,2])
    [-2, 2]
    """

    divisors = []
    for denominator in possible_divisors:
        if denominator != 0 and num % denominator == 0:
            divisors.append(denominator)

    return divisors