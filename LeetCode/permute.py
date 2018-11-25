# Given a collection of distinct numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#####################################################
class Solution(object):

	def permute(self,nums):
		if len(nums)==1:
			return [nums]

		new_permutes = []
		for idx,x in enumerate(nums):
			t = list(nums)
			t.pop(idx)
			permutes = self.permute(t)
			for i in permutes:
				new_permutes.append(i + [x])
		return new_permutes

	def permute_dp(self,nums):
		permutes = [[]]
		for _ in range(len(nums)):
			for num in nums:
				for perm in permutes:
					perm += [num]
		return permutes




def main():
	nums = [1,2,3]
	sol = Solution()
	print(sol.permute_dp(nums))


if __name__ == '__main__':
	main()
