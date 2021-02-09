# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def dfs(root,upper,lower):
            if not root:
                return True
            if upper!=None:
                if root.val>=upper:
                    return False
            if lower!=None:
                if root.val<=lower:                 
                    return False
                
            left = dfs(root.left,root.val,lower)
            if left:
                right = dfs(root.right,upper,root.val)
            if left and right:
                return True
            else:
                return False
            
        return dfs(root,None,None)