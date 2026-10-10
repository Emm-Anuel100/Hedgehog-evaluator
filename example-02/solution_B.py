def sum_range(n: int) -> int:
    """
    O(n) implementation. 
    Will fail/timeout for N = 10^18.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
