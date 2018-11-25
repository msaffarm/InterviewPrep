# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a 
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.

# Example 1:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4 
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
################################

# TC: O(m*n)
# SC: O(m)
import os
import sys

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
UTIL_PATH = CURRENT_DIR + "/../util/"
sys.path.append(UTIL_PATH)
from Tree import BT


class Solution(object):


  def isSubTree(self,s,t):
    if self._is_equal(s,t):
      return True

    if s.left and s.right:
      return self.isSubTree(s.left,t) or self.isSubTree(s.right,t)
    elif s.left:
      return self.isSubTree(s.left,t)
    elif s.right:
      return self.isSubTree(s.right,t)
    else:
      return False


  def _is_equal(self,s,t):
    
    if not s and not t:
      return True
    if (not s and t) or (not t and s):
      return False  
    if t.data != s.data:
      return False
    
    return self._is_equal(s.left,t.left) and self._is_equal(s.right,t.right)


def main():
  s = BT()
  vals = [1,2,3,4,5,6]
  for x in vals:
    s.insert(x)
  s.print_in_order(s.get_root())
  print()

  t = BT()
  valt = [3,]
  for x in valt:
    t.insert(x)
  t.print_in_order(t.get_root())
  print()


  sol = Solution()
  print(sol.isSubTree(s.get_root(),t.get_root()))
  # print(sol._is_equal(s.get_root(),t.get_root()))


if __name__ == '__main__':
  main()

