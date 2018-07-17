
# coding: utf-8

# In[ ]:

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # two pointers: walker and runner, walker moves 1 each time, and runner moves 2
        # if there is a circle in linklist, then they can meet sometime
        walker, runner = head, head
        while walker and walker.next and runner and runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False