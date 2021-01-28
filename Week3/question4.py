class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                print('l',S)
                backtrack(S+'(', left+1, right)
            if right < left:
                print('r',S)
                backtrack(S+')', left, right+1)

        backtrack()
        return ans