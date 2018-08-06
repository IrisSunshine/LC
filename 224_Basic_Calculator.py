
# coding: utf-8

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
#         def compute(s):
#             ans, temp, prev = 0, 0, 1
#             m = 0
#             for i in range(len(s)):
#                 if ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
#                     temp *= 10
#                     temp += int(s[i])
#                     m = 0
#                 elif s[i] == '+' or s[i] == '-':
#                     if not m:
#                         ans += prev * temp
#                         temp = 0
#                         prev = 1 if s[i] == '+' else -1
#                         if s[i] == '-':
#                             m = 1
#                     elif s[i] == '-':
#                         prev *= -1
#             ans += prev * temp
#             return ans
        
#         ret, top = '', 0
#         for i in range(len(s)):
#             if s[i] == ')':
#                 for j in range(top - 1, - 1, - 1):
#                     if ret[j] == '(':
#                         break
#                 ret = ret[:j] + str(compute(ret[j + 1:top]))
#                 top = len(ret)
#             else:
#                 ret += s[i]
#                 top += 1
#         return compute(ret)


        ans, temp, p = 0, 0, 1
        nums, ops = [], []
        for c in s:
            if c.isdigit():
                temp = 10 * temp + int(c)
            elif c == '+' or c == '-':
                ans += p * temp
                temp, p = 0, 1 if c == '+' else -1
            elif c == '(':
                nums.append(ans)
                ops.append(p)
                ans, p = 0, 1
            elif c == ')':
                temp = ans + p * temp
                ans, p = nums.pop(), ops.pop()
        return ans + p * temp

            
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.calculate('(1+(4+5+2)-3)+(6+8)')
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))