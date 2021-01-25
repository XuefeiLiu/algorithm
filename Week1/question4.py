class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N==1:
            return 0
        if self.kthGrammar(N-1, (K+1)/2) ==0:
            return 1-K%2
        else:
            return K%2