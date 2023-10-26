# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        cur2 = head
        res = head
        c = 0
        # Count the number of nodes in LL
        while(cur):
            c+=1
            cur=cur.next
        
        # Calculating the node index to be removed
        indexToRemove = c - n

        #If only one element is present in the LL
        if c==1:
            return None

        # If first index needs to be removed
        elif indexToRemove == 0:
                return res.next
                
        else:
            c1 = 0

            # Traversing to the node prev to node that needs to be removed
            while(c1<indexToRemove-1):
                c1+=1
                cur2=cur2.next

            
            # Removing node which is not at first index
            if cur2 and cur2.next:
                cur2.next = cur2.next.next
            
            
            return res
