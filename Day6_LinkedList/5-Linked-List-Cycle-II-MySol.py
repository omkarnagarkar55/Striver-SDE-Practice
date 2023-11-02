# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Solution
# Added the node into a list if not present
# If the node is present in the list then the loop exist and simply return current node
# If no loop found then return NULL i.e return cur when cur is NULL

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        m = []
        while cur:
            if cur in m:
                return cur
            else:
                m.append(cur)
            cur=cur.next
        
        return cur
