from __future__ import annotations
from typing import List


def is_valid(s: str) -> bool:
    """Check if parentheses string is valid."""
    pairs = {')': '(', ']': '[', '}': '{'}
    stack: List[str] = []
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        else:
            if not stack or stack.pop() != pairs.get(ch):
                return False
    return not stack


if __name__ == "__main__":
    print(is_valid("()[]{}"))
    print(is_valid("(]"))
