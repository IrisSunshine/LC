
# coding: utf-8

class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        
        eng_1 = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten',
                 'Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        eng_2 = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        ans = []
        s = str(num).zfill(10)
        n = [int(s[0]), int(s[1:4]), int(s[4:7]), int(s[7:10])]
        
        def Num_in_1000(num):
            ans = []
            if num >= 100:
                ans.append(eng_1[num // 100 - 1] + ' Hundred')
                num %= 100
            if num >= 20:
                ans.append(eng_2[num // 10 - 2])
                num %= 10
            if num > 0:
                ans.append(eng_1[num - 1])
            return ans
        
        if n[0]:
            ans.append(eng_1[n[0] - 1] + ' Billion')
        if n[1]:
            ans += Num_in_1000(n[1])
            ans.append('Million')
        if n[2]:
            ans += Num_in_1000(n[2])
            ans.append('Thousand')
        if n[3]:
            ans += Num_in_1000(n[3])
        return ' '.join(ans)
            
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.numberToWords(1234567890)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))