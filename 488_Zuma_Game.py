
# coding: utf-8

class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        import collections
        hand_counter = collections.Counter(hand)
        ans = self.process(board + '$', hand_counter)
        return ans if ans < 6 else -1

    def process(self, board, hand):
        board = self.remove(board)
        if board == '$': return 0
        count, i = 6, 0
        for j in range(1, len(board)):
            if board[i] != board[j]:
                ball = 3 - (j-i)
                if hand[board[i]] >= ball:
                    hand[board[i]] -= ball
                    count = min(count, ball + self.process(board[:i]+board[j:], hand))
                    hand[board[i]] += ball
                i = j
        return count

    def remove(self, board):
        i = 0
        for j in range(1, len(board)):
            if board[i] != board[j]:
                if j - i >= 3:
                    return self.remove(board[:i] + board[j:])
                i = j
        return board

if __name__ == "__main__":
    from time import time
    sol = Solution()
    t = time()
    ans = sol.findMinStep("RBYYBBRRB", "YRBGB")
    print('ans: %s\ntime: %.3fms' % (ans, ((time() - t)) * 1000))