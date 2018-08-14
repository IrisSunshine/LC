
# coding: utf-8

class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = []
        self.size = k
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.queue.append(value)
            return True
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.queue.pop(0)
            return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[0]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[-1]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return len(self.queue) == 0
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return len(self.queue) == self.size
        

if __name__ == "__main__":
    obj = MyCircularQueue(3)
    print(obj.enQueue(1))
    print(obj.enQueue(2))
    print(obj.enQueue(3))
    print(obj.enQueue(4))
    print(obj.Rear())
    print(obj.isFull())
    print(obj.deQueue())
    print(obj.enQueue(4))
    print(obj.Rear())