from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        leftNode = None
        rightNode = None
        prev = None
        count = 0
        curr = head

        while curr:
            count += 1 
            if count < left:
                leftNode = curr
                curr = curr.next
                continue
            elif count > right:
                rightNode = curr
                break
            elif count == left:
                lastNode = curr
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        if leftNode:
            leftNode.next = prev
        else: 
            head = prev
        
        if rightNode:
            lastNode.next = rightNode

        return head




list1 = [1,2]

def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


out = Solution().reverseBetween(lst2link(list1), 1, 2)
output = []
while out:
    output.append(out.val)
    out = out.next

print(output)
        