from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:  # pragma: no cover
        return f"ListNode({self.val})"


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Iteratively reverse a singly linked list."""
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


if __name__ == "__main__":
    n3 = ListNode(3)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    rev = reverse_list(n1)
    # Print reversed list values
    vals = []
    while rev:
        vals.append(rev.val)
        rev = rev.next
    print(vals)
