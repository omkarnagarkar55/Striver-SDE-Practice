# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = list1
        j = list2
        dd = ListNode(0,None)
        d = ListNode(0,next = dd)
        while(i!=None and j!= None):
            if i.val <= j.val:
                dd.next = i
                i=i.next
            else:
                dd.next = j
                j = j.next

            dd = dd.next
        
        if(i!=None):
            while(i):
                dd.next = i
                i=i.next
                dd=dd.next
        
        if(j!=None):
            while(j):
                dd.next = j
                j=j.next
                dd=dd.next
        
        return  d.next.next
            

        