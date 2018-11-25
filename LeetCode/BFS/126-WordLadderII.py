import os
import sys
from collections import deque
import string
alphabet = string.ascii_lowercase

class Solution(object):
	def findLadders(self, beginWord, endWord, wordList):
		wordListset = set(wordList)
		queue = deque()
		queue.append(beginWord)
		visited = set()
		cur_ladder = []
		ladders = []
		while queue:
			cur_node = queue.popleft()
			if cur_node in visited:
				continue
			if cur_node in wordList:
				cur_ladder.append(cur_node)
			for i,c in enumerate(cur_node):
				for char in alphabet:
					new_node = cur_node[:i] + char + cur_node[i:]
					if new_node in wordList:
						queue.apppend(new_node)
			visited.add(cur_node)


def main():
	s = Solution()
	start = "hit"
	end = "cog"
	word_list = ["hot","dot","dog","lot","log","cog"]
	print(s.ladderLength(start,end,word_list))


if __name__ == '__main__':
	main()