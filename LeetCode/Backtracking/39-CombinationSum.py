# Given a set of candidate numbers (C) (without duplicates) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7, 
# A solution set is: 
# [
#   [7],
#   [2, 2, 3]
# ]
#####################################################################################
class Solution(object):
	def combinationSum(self, candidates, target):
		sols,s = [],[]
		# self.backtrack(s,candidates,0,target,sols)
		self.fast_backtrack(s,sorted(candidates),0,target,sols)
		return sols
	# def backtrack(self,s,candidates,sum,target,sols):
	# 	if sum==target:
	# 		sols.add(tuple(sorted(s)))
	# 		return
	# 	for can in candidates:
	# 		if sum+can > target:
	# 			continue
	# 		self.backtrack(s + [can],candidates,sum+can,target,sols)

	def fast_backtrack(self,s,candidates,sum,target,sols):
		# candidates are sorted! nice trick
		if sum==target:
			sols.append(s)
			return
		for can in candidates:
			if sum+can > target:
				break
			if s and can < s[-1]:
				continue
			self.fast_backtrack(s + [can],candidates,sum+can,target,sols)



def main():
	sol = Solution()
	candidates = [2,3,6,7]
	target = 7
	print("hello!")
	print(sol.combinationSum(candidates,target))


if __name__ == '__main__':
	main()