# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        s  =''
        # Itterate through the LL and concatinate the value to a string variable
        while cur:
            s += str(cur.val)
            cur=cur.next

        # check if reverse is same as the string
        
        if s[::-1] == s:
            return True
        else:
            return False