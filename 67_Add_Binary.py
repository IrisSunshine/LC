
# coding: utf-8

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
#         if len(a) > len(b):
#             b = b.zfill(len(a))
#         else:
#             a = a.zfill(len(b))
        
#         c = 0
#         ans = ''
#         for i in range(len(a) - 1, -1, -1):
#             d = int(a[i]) ^ int(b[i]) ^ int(c)
#             c = 1 if int(a[i]) + int(b[i]) + int(c) > 1 else 0
#             ans = str(d) + ans
#         if c:
#             ans = str(c) + ans
#         return ans

        return (bin(int(a, 2) + int(b, 2))[2:])
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.addBinary(a = "11", b = "1")
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))