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
        cur = head
        cur2 = head
        m = {}
        while(cur):
            m[cur] = Node(cur.val,None,None)
            cur =cur.next
        while(cur2):
            if cur2.next:
                m[cur2].next = m[cur2.next]
            else:
                m[cur2].next = None
            if cur2.random:
                m[cur2].random = m[cur2.random]
            else:
                m[cur2].random = None
            cur2=cur2.next
        if head:
            return m[head]
        else:
            return head