# 530. Minimum Absolute Difference in BST
# Given a binary search tree with non-negative values, find the minimum
 # absolute difference between values of any two nodes.

# Example:

# Input:

#    1
#     \
#      3
#     /
#    2

# Output:
# 1

# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 
# (or between 2 and 3).
# ###################33

class TreeNode(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):

	def getMinimumDifference(self, root):
		



	def print_inorder(self,root):
		if not root:
			return
		self.print_inorder(root.left)
		print(root.val, end=" ")
		self.print_inorder(root.right)


def main():
	s = Solution()
	root = TreeNode(1)
	root.right = TreeNode(3)
	root.right.left = TreeNode(2)
	s.print_inorder(root)


if __name__ == '__main__':
	main()