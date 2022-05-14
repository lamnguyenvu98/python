from typing import List

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertNode(lst: List):
    head = ListNode()
    curr = head
    for l in lst:
        curr.val = l
        curr.next = ListNode()
        curr = curr.next
    return head

def NodetoList(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

def addTwoNumbers(l1: List, l2: List):
    head_l1 = insertNode(l1)
    head_l2 = insertNode(l2)
    
    head_res = ListNode()
    curr = head_res
    
    carry = 0
    
    while head_l1 or head_l2 or carry:
        val_1 = head_l1.val if head_l1 else 0
        val_2 = head_l2.val if head_l2 else 0
        
        sum_ = val_1 + val_2 + carry
        carry = sum_ // 10
        sum_ = sum_ % 10
        curr.next = ListNode(sum_)
        
        curr = curr.next
        head_l1 = head_l1.next
        head_l2 = head_l2.next
    
    res = NodetoList(head_res.next)
    return res

l1 = [1, 2, 4]
l2 = [4, 5, 6]
res = addTwoNumbers(l1, l2)
print(res)



