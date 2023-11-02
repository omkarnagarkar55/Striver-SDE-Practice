# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur  = head
        l = []
        flag = False
        while cur:
            if cur in l:
                flag = True
                break
            else:
                l.append(cur)

            cur=cur.next
        return flag