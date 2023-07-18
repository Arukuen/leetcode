

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    list1 = []
    list2 = []

    while l1:
        list1.append(l1.val)
        l1 = l1.next

    while l2:
        list2.append(l2.val)
        l2 = l2.next

    int1 = int(''.join(map(str, list1)))
    int2 = int(''.join(map(str, list2)))

    sum = int1 + int2

    curr = dummy = ListNode(0)
    for n in str(sum):
        curr.next = ListNode(int(n))
        curr = curr.next
    return dummy.next
    


        
l1 = [2,4,3]
l2 = [5,6,4]

def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


out = addTwoNumbers(lst2link(l1), lst2link(l2))
output = []
while out:
    output.append(out.val)
    out = out.next

print(output)