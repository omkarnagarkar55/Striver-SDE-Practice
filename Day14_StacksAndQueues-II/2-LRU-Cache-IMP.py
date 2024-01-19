# To Build a LRU Cache we need to use DLL and a hashmap
class LRUCache:
    # Creating Node for DLL and initializing it.
    class Node:
        def __init__(self,key,val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.h = {}
        
    # Add element to the front
    def addNode(self, newnode):
        temp = self.head.next
        newnode.next = temp
        newnode.prev = self.head
        self.head.next = newnode
        temp.prev = newnode

    # Delete element from the back
    def deleteNode(self, delnode):
        prevv = delnode.prev
        nextt = delnode.next
        prevv.next = nextt
        nextt.prev = prevv

    def get(self, key: int) -> int:
        # If key already exist then del and add it to the front
        if key in self.h:
            resNode = self.h[key]
            ans = resNode.val
            del self.h[key]
            self.deleteNode(resNode)
            self.addNode(resNode)
            self.h[key] = self.head.next
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        # If element already exist then delete the element and add a new one at front.
        if key in self.h:
            curr = self.h[key]
            del self.h[key]
            self.deleteNode(curr)

        # When list to full then remove the element from the back
        if len(self.h) == self.cap:
            del self.h[self.tail.prev.key]
            self.deleteNode(self.tail.prev)

        self.addNode(self.Node(key, value))
        self.h[key] = self.head.next        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)