class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # dummy refers to the dummy head, the real linked list starts at the dummy head
    curr_out = dummy = ListNode(0)
    curr1 = l1
    curr2 = l2
    carry = 0
    while True:
        curr_out.next = ListNode(0)
        curr_out = curr_out.next

        curr_out.val = curr1.val + curr2.val + carry

        if curr_out.val > 9:
            carry = 1
            curr_out.val -= 10
        else: carry = 0

        if not curr1.next and not curr2.next:
            if carry > 0: curr_out.next = ListNode(carry)
            return dummy.next

        if curr1.next: curr1 = curr1.next
        else: curr1 = ListNode(0)
        if curr2.next: curr2 = curr2.next
        else: curr2 = ListNode(0)

        
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


out = addTwoNumbers(lst2link(l1), lst2link(l2))
while out:
    print(out.val)
    out = out.next