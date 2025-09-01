from __future__ import annotations
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of the two numbers that add up to target."""
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
