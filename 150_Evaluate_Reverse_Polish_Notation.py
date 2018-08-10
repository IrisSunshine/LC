
# coding: utf-8

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ret = []
        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                b = ret.pop()
                a = ret.pop()
                if tokens[i] == '+':
                    c = a + b
                elif tokens[i] == '-':
                    c = a - b
                elif tokens[i] == '*':
                    c = a * b
                else:
                    c = int(a / b)
                ret.append(c)
            else:
                ret.append(int(tokens[i]))
        return ret[0]
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))