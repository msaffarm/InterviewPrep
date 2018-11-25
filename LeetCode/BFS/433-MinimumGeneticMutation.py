import os
import sys
from collections import deque
bases = ["A","C","G","T"]

class Solution(object):
	def minMutation(self,start,end,bank):
		bankSet = set(bank)
		queue = deque()
		visited = set()
		queue.append((start,0))
		while queue:
			cur_node,depth = queue.popleft()
			if cur_node in visited:
				continue
			if cur_node==end:
				return depth
			for i,c in enumerate(cur_node):
				for b in bases:
					mutation = cur_node[:i] + b + cur_node[i+1:]
					if mutation in bankSet:
						queue.append((mutation,depth+1))
			visited.add(cur_node)
		return -1 



# class Solution(object):
# 	def minMutation(self,start,end,bank):
# 		queue = deque()
# 		visited_nodes = set()
# 		queue.append(start)
# 		while queue:
# 			cur_node = queue.popleft()
# 			if cur_node in visited_nodes:
# 				continue
# 			for ch in start:
# 				all_possible_bases = [x for x in bases if x!=ch]
# 				new_comb = 






def main():
	s = Solution()
	bank=["AACCGGTA","AACCGCTA","AAACGGTA"]
	start="AACCGGTT"
	end="AAACGGTA"
	print(s.minMutation(start,end,bank))


if __name__ == '__main__':
	main()