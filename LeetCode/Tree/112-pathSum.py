# Given a binary tree and a sum, determine if the tree has a root-to-leaf
#  path such that adding up all the values along the path equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
###############################################################################
import os
import sys

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
UTIL_PATH = CURRENT_DIR + "/../util/"
sys.path.append(UTIL_PATH)
from Tree import BT

class Solution(object):

	def hasPathSum(self,root,sum):

		# for handling empty tree
		if not root:
			return False
		if root.right and root.left:
			return self.hasPathSum(root.left,sum-root.data) or self.hasPathSum(root.right,sum-root.data)
		elif root.right:
			return self.hasPathSum(root.right,sum-root.data)
		elif root.left:
			return self.hasPathSum(root.left,sum-root.data)
		else:
			return sum==root.data


def main():
	s = BT()
	vals = [1,2,3,4,5,6]
	for x in vals:
		s.insert(x)
	s.print_in_order(s.get_root())
	print()

	sol = Solution()
	print(sol.hasPathSum(s.get_root(),10))


if __name__ == '__main__':
	main()


