# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1 = l1
        ll2 = l2
        dd = ListNode(0,None)
        temp = dd
        carry = 0
        while ll1 or ll2 or carry == 1:
            s = 0
            if ll1:
                s+=ll1.val
                ll1=ll1.next
            if ll2:
                s+=ll2.val
                ll2=ll2.next
            
            s+=carry
            carry = s//10
            node = ListNode(s % 10,None)
            temp.next = node
            temp = temp.next
        return dd.next