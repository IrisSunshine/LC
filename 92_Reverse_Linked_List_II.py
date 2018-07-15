
# coding: utf-8

# In[ ]:

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        start = head
        first = None
        last = None
        node = head
        for i in range(1, n+1):
            next_node = node.next
            if i == m-1:
                start = node
            elif i == m:
                first = node
                last = node
            elif i > m:
                node.next = first
                first = node
            node = next_node
        last.next = node
        if last is head:
            return first
        start.next = first
        return head

