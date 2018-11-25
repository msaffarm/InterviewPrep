# Given two words (beginWord and endWord), and a dictionary's word list, find all
# shortest transformation sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a
# transformed word.
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
##################################################################################
import string 
lowercase = string.ascii_lowercase
from collections import deque

# class Solution(object):
# 	def findLadders(self, beginWord, endWord, wordList):
# 		wordList = set(wordList)
# 		sols = []
# 		def backtrack(endWord,wordList,s,sols):
# 			# does not work! we want shortest solutions
# 			last_word = s[-1]
# 			if last_word==endWord:
# 				sols.append(s)
# 				return
# 			for char in lowercase:
# 				for idx,_ in enumerate(last_word):
# 					new_word = last_word[:idx] + char + last_word[idx+1:]
# 					if new_word in wordList and new_word not in s:
# 						backtrack(endWord,wordList,s+[new_word],sols)


# 		backtrack(endWord,wordList,[beginWord],sols)
# 		return sols


# BFS of paths not words!
class Solution(object):
	def findLadders(self, beginWord, endWord, wordList):
		wordList = set(wordList)
		if endWord not in wordList:
			return []
		wordList.add(beginWord)
		visited = set()
		queue = deque()
		queue.append([beginWord])
		goal_level = None
		level=1
		sols = []
		while queue:
			cur_path = queue.popleft()
			if goal_level:
				if len(cur_path)>=goal_level:
					continue
			if len(cur_path)>level:
				for node in visited:
					wordList.remove(node)
				visited.clear()
				level+=1

			last_word = cur_path[-1]
			for char in lowercase:
				for idx,_ in enumerate(last_word):
					new_word = last_word[:idx] + char + last_word[idx+1:]
					if new_word==endWord:
						if not goal_level:
							goal_level = len(cur_path)+1
						sols.append(cur_path + [new_word])
						continue
					if new_word in wordList and new_word not in cur_path:
						queue.append(cur_path + [new_word])
			visited.add(last_word)

		return sols




def main():
	# beginWord,endWord="hit","cog"
	# wordList=["hot","dot","dog","lot","log","cog"]
	# beginWord,endWord="a","d"
	# wordList=["a","b","c","d"]
	beginWord,endWord="red","tax"
	wordList=["ted","tex","red","tax","tad","den","rex","pee"]
	sol = Solution()
	print(sol.findLadders(beginWord,endWord,wordList))


if __name__ == '__main__':
	main()