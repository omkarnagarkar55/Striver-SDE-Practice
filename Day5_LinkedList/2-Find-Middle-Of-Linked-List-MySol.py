# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        length = 0
        while(cur):
            length+=1
            cur = cur.next
        
        mid = None
        if length % 2 != 0:
            mid = int((length + 1)/2)
        else:
            mid = int((length/2) + 1)
        
        print(mid)
        midNode =head
        c = 0
        while(c<mid-1):
            midNode = midNode.next
            c+=1

        return midNode
        
        