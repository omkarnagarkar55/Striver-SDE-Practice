class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        entry = head

        if(head == None or head.next == None): 
            return None

        while(fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next
            if(slow == fast):
                while(slow!=entry):
                    entry=entry.next
                    slow=slow.next
                return slow

        return None