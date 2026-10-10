from typing import List, Optional

def find_first_duplicate(nums: List[int]) -> Optional[int]:
    """
    O(n) time and O(n) space using a set.
    """
    seen = set()
    for n in nums:
        if n in seen:
            return n
        seen.add(n)
    return None
