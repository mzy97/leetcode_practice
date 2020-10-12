#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    pre = 999
    diff = 999

    def getMinimumDifference(self, root: TreeNode) -> int:

        def Search(root):
            if root == None:
                return

            Search(root.left)
            self.diff = min(self.diff, abs(self.pre - root.val))
            self.pre = root.val
            Search(root.right)

        Search(root)

        return self.diff

# @lc code=end

