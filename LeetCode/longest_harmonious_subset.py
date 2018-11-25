# We define a harmonious array is an array where the difference between 
# its maximum value and its minimum value is exactly 1.

# Now, given an integer array, you need to find the length of its longest harmonious
# subsequence among all its possible subsequences.

# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
###################################################################
# TC = O(nlgn) due to sorting
# SC = O(n) due to hashmap

# class Solution(object):

# 	def findLHS(self,nums):
# 		temp_dict = {}
# 		for x in nums:
# 			if x in temp_dict:
# 				temp_dict[x] += 1
# 			else:
# 				temp_dict[x] = 1
# 		# sort dict
# 		sorted_dict = sorted(temp_dict.items(),key=lambda x:x[0])
# 		# find maximum subset lenght
# 		max_len = 0
# 		for i in range(len(sorted_dict)-1):
# 			if sorted_dict[i+1][0]-sorted_dict[i][0]==1:
# 				max_len = max(max_len,sorted_dict[i][1]+sorted_dict[i+1][1])

# 		return max_len
#######################################
# TC = O(n)
# SC = O(n)

class Solution(object):

	def findLHS(self,nums):
		temp_dict = {}
		for x in nums:
			if x in temp_dict:
				temp_dict[x] += 1
			else:
				temp_dict[x] = 1

		max_len = 0
		for key in temp_dict:
			if key+1 in temp_dict:
				max_len = max(max_len,temp_dict[key]+temp_dict[key+1])

		return max_len

def main():
	s = [1,3,2,2,2,5,7]
	sol = Solution()
	print(sol.findLHS(s))



if __name__ == '__main__':
	main()