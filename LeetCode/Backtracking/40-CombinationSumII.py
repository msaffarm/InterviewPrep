# Given a collection of candidate numbers (C) and a target number (T), find all
# unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
# A solution set is: 
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
###############################################################################
class Solution(object):
	def combinationSum2(self, candidates, target):
		sols,s = set(),[]
		self.fast_backtrack(s,sorted(candidates),0,target,sols,0,len(candidates)-1)
		return sols

	def fast_backtrack(self,s,candidates,sum,target,sols,start,end):
		# candidates are sorted! nice trick
		if sum==target:
			sols.add(tuple(sorted([candidates[x] for x in s])))
			return
		if start==end+1:
			return
		for idx,can in enumerate(candidates):
			if idx in s:
				continue
			if sum+can > target:
				break
			self.fast_backtrack(s + [idx],candidates,sum+can,target,sols,start+1,end)


def main():
	sol = Solution()
	# [10, 1, 2, 7, 6, 1, 5]
	candidates = [10, 1, 2, 7, 6, 1, 5]
	target = 8
	print(sol.combinationSum2(candidates,target))


if __name__ == '__main__':
	main()