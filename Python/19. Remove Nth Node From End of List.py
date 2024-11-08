from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_n = dummy
        curr = head
        i = 1
        while curr.next is not None:
            if i >= n:
                prev_n = prev_n.next
            curr = curr.next
            i += 1
        prev_n.next = prev_n.next.next
        return dummy.next
    
list1 = [1,2,3,4]

def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


out = Solution().removeNthFromEnd(lst2link(list1), 2)
output = []
while out:
    output.append(out.val)
    out = out.next

print(output)
        
