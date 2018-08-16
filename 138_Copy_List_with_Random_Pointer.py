
# coding: utf-8

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        
        new_head = RandomListNode(head.label)
        cur_node = new_head
        node = head.next
        hmap = dict()
        hmap[head] = new_head
        
        while node:
            new_node = RandomListNode(node.label)
            cur_node.next = new_node
            cur_node = cur_node.next
            hmap[node] = cur_node
            node = node.next
            
        node, cur_node = head, new_head
        while node:
            if node.random != None:
                cur_node.random = hmap[node.random]
            cur_node = cur_node.next
            node = node.next
        return new_head
            
if __name__ == "__main__":
    sol = Solution()
    a1,a2,a3,a4,a5 = RandomListNode(1),RandomListNode(2),RandomListNode(3),RandomListNode(4),RandomListNode(5)
    a1.next,a2.next,a3.next,a4.next = a2,a3,a4,a5
    a1.random,a2.random,a3.random,a4.random,a5.random = a5,a1,a3,None,a1
    ans = sol.copyRandomList(a1)
    while ans:
        print('label = %s, next = %s, random = %s'
              %(ans.label,'None' if not ans.next else 'a' + str(ans.next.label),'None' if not ans.random else 'a' + str(ans.random.label)))
        ans = ans.next