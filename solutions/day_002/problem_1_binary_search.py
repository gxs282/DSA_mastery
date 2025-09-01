from __future__ import annotations
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """Return index of target in sorted nums, else -1."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9], 7))
    print(binary_search([1, 3, 5, 7, 9], 2))
