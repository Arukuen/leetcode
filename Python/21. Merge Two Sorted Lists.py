class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Using loop
def mergeTwoLists(list1:ListNode, list2:ListNode) ->ListNode:
    dummy = curr_out = ListNode(0)
    while True:
        if list1 and list2:
            if list1.val > list2.val:
                curr_out.next = ListNode(list2.val)
                curr_out = curr_out.next
                list2 = list2.next
            else:
                curr_out.next = ListNode(list1.val)
                curr_out = curr_out.next
                list1 = list1.next
        elif list1:
            curr_out.next = ListNode(list1.val)
            curr_out = curr_out.next
            list1 = list1.next
        elif list2:
            curr_out.next = ListNode(list2.val)
            curr_out = curr_out.next
            list2 = list2.next
        else:
            return dummy.next

# Using recursion  
def mergeTwoLists(list1:ListNode, list2:ListNode) ->ListNode:
    if not list1: return list2
    elif not list2: return list1
    elif list1.val > list2.val:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2
    else:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1




list1 = [1,2,4]
list2 = [1,3,4]

def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


out = mergeTwoLists(lst2link(list1), lst2link(list2))
output = []
while out:
    output.append(out.val)
    out = out.next

print(output)
        
