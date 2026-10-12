# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev=None
        difference=None
        list_diff=[]
        def ios(root):
            nonlocal prev
            nonlocal list_diff
            nonlocal difference
            if root is None:
                return
            ios(root.left)
            current=root.val
            if prev is not None:
                difference=current-prev
                list_diff.append(difference)
            prev=current
            ios(root.right)
        ios(root)
        print(list_diff)
        return min(list_diff)


        