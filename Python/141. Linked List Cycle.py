from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash = set()
        while head:
            if id(head) in hash:
                return True
            if head.next:
                hash.add(id(head))
            head = head.next
        return False