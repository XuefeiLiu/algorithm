class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        def back(s,left,right):
            if len(s) == 2*n:
                results.append(s)
                return
            if left<n:
                back(s+'(',left+1,right)
            if right<left:
                back(s+')',left,right+1)
        back('',0,0)
        return results