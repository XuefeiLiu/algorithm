# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = deque([(root,1)])
        result = {1:root.val}
        while queue:
            node,depth = queue.popleft()
            if node.left:
                queue.append((node.left,depth+1))
                result[depth+1] = node.left.val
            if node.right:
                queue.append((node.right,depth+1))
                result[depth+1] = node.right.val
        k = result.keys()
        k.sort()
        final = []
        for i in k:
            final.append(result[i])
        return final