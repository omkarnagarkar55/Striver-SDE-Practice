# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = cur2 = head
        l = []

        # Store all the node values in a linked list
        while cur:
            l.append(cur.val)
            cur = cur.next
        
        # Reverse values from i to k and store it in list
        n = len(l)
        i = 0
        while(i < n):
            if i+k<=n:
                rev = l[i:i+k][::-1]
                l[i:i+k] = rev
            else:
                break
            i = i + k
        
        # Store all the values from l to the linked list
        c = 0
        print (l)
        while cur2 and c <n:
            cur2.val = l[c]
            c+=1
            cur2 = cur2.next
        
        return head