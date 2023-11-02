# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        h = {}
        a1 = headA
        b1 = headB

        while a1:
            h[a1] = a1.val
            a1=a1.next
  
        while b1:
            if b1 in h and h[b1] == b1.val:
                return b1
            b1=b1.next
