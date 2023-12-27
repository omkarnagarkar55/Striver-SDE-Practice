"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur3 = cur2 = cur  = head
        cpy = Node(0,None,None)

        # Step 1
        # Insert new node after every node. The node contains the value of its previous node
        if head:
            while(cur):
                temp = cur.next
                cur.next = Node(cur.val,temp,None)
                cur = cur.next.next
            cpy.next = cur2.next

            # Step 2
            # Set random pointer for new nodes
            while(cur2):
                if cur2.random:
                    cur2.next.random = cur2.random.next
                else:
                    cur2.next.random = None
                cur2 = cur2.next.next

            # Step 3
            # Seperate out the two linked list 
            cpy2 = cpy.next
            while(cur3):
                if cur3.next:
                    cur3.next = cur3.next.next
                else:
                    cur3.next = None
                if cpy2.next:
                    cpy2.next =cpy2.next.next
                else:
                    cpy2.next = None
                cur3 = cur3.next
                cpy2 = cpy2.next
        return cpy.next
