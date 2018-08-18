
# coding: utf-8

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
#         start = image[sr][sc]
#         if start == newColor:
#             return image
#         cur_pixels = [[sr, sc]]
#         while cur_pixels:
#             temp = []
#             for p in cur_pixels:
#                 image[p[0]][p[1]] = newColor
#                 if p[0] > 0:
#                     if image[p[0] - 1][p[1]] == start:
#                         image[p[0] - 1][p[1]] = newColor
#                         temp.append([p[0] - 1, p[1]])
#                 if p[0] < len(image) - 1:
#                     if image[p[0] + 1][p[1]] == start:
#                         image[p[0] + 1][p[1]] = newColor
#                         temp.append([p[0] + 1, p[1]])
#                 if p[1] > 0:
#                     if image[p[0]][p[1] - 1] == start:
#                         image[p[0]][p[1] - 1] = newColor
#                         temp.append([p[0], p[1] - 1])
#                 if p[1] < len(image[0]) - 1:
#                     if image[p[0]][p[1] + 1] == start:
#                         image[p[0]][p[1] + 1] = newColor
#                         temp.append([p[0], p[1] + 1])
#             cur_pixels = temp
#         return image
        
        if image[sr][sc] == newColor:
             return image
        self.m = len(image)
        self.n = len(image[0])
        self.image = image
        self.newColor = newColor
        self.oldColor = image[sr][sc]
        
        def DFS(r, c):
            if r == -1 or r == self.m or c == -1 or c == self.n or self.image[r][c] != self.oldColor:
                return
            self.image[r][c] = self.newColor
            DFS(r - 1, c)
            DFS(r + 1, c)
            DFS(r, c - 1)
            DFS(r, c + 1)
            return
        
        DFS(sr, sc)
        return image
    
if __name__ == "__main__":
    from time import time
    sol = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    t = time()
    ans = sol.floodFill(image, sr, sc, newColor)
    print('ans = %s\ntime = %.3fms'%(ans, (time() - t) * 1000))