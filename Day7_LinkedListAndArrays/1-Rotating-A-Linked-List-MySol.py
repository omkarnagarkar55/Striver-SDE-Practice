# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur3 = head
        l=0

        # Calculating the length of the linked list
        while cur3:
            l+=1
            cur3=cur3.next

        # If the length of linked list is zero then return the head
        if l==0:
            return head
        else:
            # If k is greater than the length of the array,
            # then just use the remainder - k % l as LL will keep repeating itself 
            count =0
            if k > l:
                count = k % l
            else:
                count = k
            
            # Rotating the linked list
            i = 0
            while i < count: 
                preVal = 0
                cur = head
                cur2 = head
                # copying the value of previous node to cur node and storing the value of current node in previous before moving to next node.
                while cur:
                    t = cur.val
                    cur.val = preVal
                    preVal = t 
                    cur = cur.next

                    # Copying the value of last node into first
                    cur2.val = preVal
                i+=1
            return head
        