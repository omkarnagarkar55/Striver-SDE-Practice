# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1 = l1
        ll2 = l2
        val1 =''
        val2 =''
        while(ll1):
            val1+=str(ll1.val)            
            ll1=ll1.next

        while(ll2):
            val2+=str(ll2.val)
            ll2=ll2.next
        
        s = int(val1[::-1]) +int(val2[::-1])

        dd = ListNode( 0,None)
        d = dd
        if s == 0:
            return dd
        else:
            while(s>0):
                lastNo = s % 10
                d.next = ListNode(lastNo,None)
                d = d.next
                s=s//10

        return dd.next