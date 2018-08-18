
# coding: utf-8

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        ans = set()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return list(ans)
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.intersection([4,9,5], [9,4,9,8,4])
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))