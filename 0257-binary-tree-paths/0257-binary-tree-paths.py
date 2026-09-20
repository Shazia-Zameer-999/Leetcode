# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        output=[]
        path=[]
        def dfs(root):
            if root is None:
                return
            path.append(root.val)
            if root.left is None and root.right is None:
                output.append("->".join(map(str, path)))


            dfs(root.left)
            dfs(root.right)
            path.pop()
        dfs(root)
        return output

        