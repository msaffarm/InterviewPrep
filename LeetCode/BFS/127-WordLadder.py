import os
import sys
from collections import deque

alphabet = "abcdefghijklmnopqrstuvwxyz"

class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		wordListSet = set(wordList)
		queue = deque()
		visited = set()
		queue.append((beginWord,0))
		while queue:
			cur_node,depth = queue.popleft()
			if cur_node in visited:
				continue
			if cur_node==endWord:
				return depth+1
			for i,c in enumerate(cur_node):
				for char in alphabet:
					child = cur_node[:i]+char+cur_node[i+1:]
					if child in wordListSet:
						queue.append((child,depth+1))
			visited.add(cur_node)
		return 0


def main():
	s = Solution()
	start = "hit"
	end = "cog"
	word_list = ["hot","dot","dog","lot","log","cog"]
	print(s.ladderLength(start,end,word_list))

if __name__ == '__main__':
	main()