from typing import List

class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.arr= [0] * 100001
    
    #  Enqueue (add) element 'e' at the end of the queue.
    def enqueue(self, e: int) -> None:
        self.rear += 1
        self.arr[self.rear] = e
        if self.front == 0:
            self.front=self.rear

    #  Dequeue (retrieve) the element from the front of the queue.
    def dequeue(self) -> int:
        temp = -1
        if self.front <= self.rear and self.front !=0:
            temp = self.arr[self.front]
            self.front+=1
        return temp