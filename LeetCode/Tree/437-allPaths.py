# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must
#  go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range
#  -1,000,000 to 1,000,000.

# Example:

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:

# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
############################################################
import os
import sys

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
UTIL_PATH = CURRENT_DIR + "/../util/"
sys.path.append(UTIL_PATH)
from Tree import BT

class Solution(object):

	def pathSum(self,x):
		pass



def main():

	s = BT()
	vals = [1,2,3,3,4,2,3]
	for x in vals:
		s.insert(x)
	s.print_in_order(s.get_root())
	print()

	sol = Solution()
	print(sol.hasPathSum(s.get_root(),6))


if __name__ == '__main__':
	main()

