# Given a list of unique words, find all pairs of distinct indices (i, j) in
#  the given list, so that the concatenation of the two words, i.e. words[i] + words[j]
#  is a palindrome.

# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]
# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
###################################################################
class Solution(object):
	
	def palindromePairs(self,words):
		pairs = []
		






def main():
	words = ["bat", "tab", "cat"]
	sol = Solution()
	print(sol.palindromePairs(words))



if __name__ == '__main__':
	main()