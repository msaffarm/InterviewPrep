class Solution(object):

	counter = 0
	memo = {}
	def findTargetSumWays(self,nums,S):
		return self.findHelper(nums,S,0,0)

	def findHelper(self,nums,target,sum,pos):
		self.counter += 1
		if pos==len(nums):
			if target==sum:
				return 1
			else:
				return 0

		if (sum,pos) in self.memo:
			return self.memo[(sum,pos)]
		else:
			val = nums[pos]
			self.memo[(sum,pos)] = self.findHelper(nums,target,sum+val,pos+1)+\
				self.findHelper(nums,target,sum-val,pos+1)
			return self.memo[(sum,pos)]


def main():
	s = Solution()
	nums = list(range(43))
	nums = [1]
	S = 1
	print(s.findTargetSumWays(nums,S))
	print(s.counter)


if __name__ == '__main__':
	main()