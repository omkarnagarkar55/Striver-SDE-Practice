# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None




class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # when list1 is empty then
        # our output will be same as list2
        if l1 == None:
            return l2


        # when list2 is empty then our output
        # will be same as list1
        if l2 == None:
            return l1


        # pointing l1 and l2 to smallest and greatest one
        if l1.val > l2.val:
            l1, l2 = l2, l1


        # act as head of resultant merged list
        res = l1


        while l1 != None and l2 != None:
            temp = None
            while l1 != None and l1.val <= l2.val:
                temp = l1 # storing last sorted node
                l1 = l1.next
            # link previous sorted node with
            # next larger node in list2
            temp.next = l2
            l1, l2 = l2, l1
        return res