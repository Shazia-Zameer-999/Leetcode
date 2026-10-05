# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
count=0
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        max_count=0
        mode=[]
        prev=None
        def inorder(root):
            nonlocal prev
            nonlocal max_count
            nonlocal mode
            global count

            if root is None:
                return
            inorder(root.left)
            current=root.val
            if current==prev:
                count+=1

            else:
                count=1

            if count>max_count:
                max_count=count
                mode=[current]
            elif count==max_count:
                mode.append(current)



            prev=current




            inorder(root.right)
        inorder(root)
        return mode
        