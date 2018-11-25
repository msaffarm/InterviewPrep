# Given a non-empty string s and a dictionary wordDict containing a list
# of non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
# You may assume the dictionary does not contain duplicate words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".


# Interesting TEST cases
# "cars"
# ["car","ca","rs"]
# ["c","a","rs"]

# "abcd"
# ["a","abc","b","cd"]


#####################################
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        temp_dict = {}
        for word in wordDict:
        	if word in temp_dict:
        		return True
        	else:
        		if s.find(word)!=-1:
	        		temp_dict[self._remove_occurances(s,word)] = None
        return "" in temp_dict


    def _remove_occurances(self,s,word):
        while True:
            idx = s.find(word)
            if idx!=-1:
                s = s[0:idx] + s[idx+len(word):]
            if s=="" or idx==-1:
                break
        return s


def main():
	d = {"a","abc","b","cd"}
	s = "abcd"
	sol = Solution()
	print(sol.wordBreak(s,d))


if __name__ == '__main__':
	main()