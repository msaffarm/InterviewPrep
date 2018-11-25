# Given a binary tree and a sum, find all root-to-leaf paths where each
#  path's sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
###############################################################################

import os
import sys

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
UTIL_PATH = CURRENT_DIR + "/../util/"
sys.path.append(UTIL_PATH)
from Tree import BT

class Solution(object):

	valid_paths = []

	def pathSum(self,root,sum):
		if self.valid_paths:
			self.valid_paths.clear()
		if not root:
			return self.valid_paths
		path = []
		self.check_paths(root,sum,path)
		return self.valid_paths

	def check_paths(self,root,sum,path):
		if root.right and root.left:
			self.check_paths(root.left,sum-root.data,path + [root.data])
			self.check_paths(root.right,sum-root.data,path + [root.data])
		elif root.left:
			self.check_paths(root.left,sum-root.data,path + [root.data])
		elif root.right:
			self.check_paths(root.right,sum-root.data,path + [root.data])
		else:
			if sum==root.data:
				self.valid_paths.append(path + [root.data])


def main():
	s = BT()
	vals = []
	for x in vals:
		s.insert(x)
	s.print_in_order(s.get_root())
	print()

	sol = Solution()
	print(sol.pathSum(s.get_root(),7))

if __name__ == '__main__':
	main()


