# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        list=[]
        def dfs(root):
            if root is None:
                return
            list.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        #to find the frequency of all the numbers from the list
        freq={}
        for i in list:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        #now to find the key which has the highest value
        max_value = max(freq.values())
        keys = [key for key, value in freq.items() if value == max_value]
        return keys
        