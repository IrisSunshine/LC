
# coding: utf-8

# In[31]:

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4:
            return []
        res = []
        self.restoreIpAddressesHelper(res, s, [], 0)
        return res
    
    def restoreIpAddressesHelper(self, res, s, temp, start):
        if len(temp) == 4 and start == len(s):
            ip = '.'.join(temp)
            res.append(ip)
            return
        if len(temp) >= 4 or start >= len(s):
            return
        self.restoreIpAddressesHelper(res, s, temp + [s[start]], start+1)
        if s[start] != '0' and start < len(s) - 1:
            self.restoreIpAddressesHelper(res, s, temp + [s[start:start+2]], start+2)
        if s[start] != '0' and start < len(s) - 2 and int(s[start:start+3]) <= 255:
             self.restoreIpAddressesHelper(res, s, temp + [s[start:start+3]], start+3)
                        
if __name__ == '__main__':
    sol = Solution()
    s  = "25525511135"
    print (s, sol.restoreIpAddresses(s))


# In[1]:

a=[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(a)


# In[7]:

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r, c = len(matrix) -1, 0
        while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            if target == matrix[r][c]:
                return True
            elif matrix[r][c] < target:
                c += 1
            else:
                r -= 1
        return False
                
if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    print (sol.searchMatrix(matrix, target))


# In[42]:




# In[ ]:



