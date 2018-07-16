
# coding: utf-8

# In[ ]:

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = []
        people.sort(key = lambda x:(-x[0],x[1]))
        
        for x in people:
            queue.insert(x[1],x)
        
        return queue
    
if __name__ == '__main__':
    sol = Solution()
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print (sol.reconstructQueue(people))

