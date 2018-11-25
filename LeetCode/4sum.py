# Given an array S of n integers, are there elements a, b, c,
# and d in S such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]




####################################
class Solution(object):
	def fourSum(self, nums, target):
		meta_dict = {}
		results = []
		for x in nums:
			if not meta_dict:
				meta_dict[(x,)] = target-x
				continue
			temp = {}
			for key,val in meta_dict.items():
				if len(key)==3:
					if val==x:
						t = list(key)
						t.append(x)
						# if not self._check_if_exists(results,t):
						results.append(t)
				elif len(key) < 3:
					t = list(tuple(key))
					t.append(x)
					temp[tuple(t)] = val-x

			meta_dict.update(temp)
			
			meta_dict[(x,)] = target-x

			# print(meta_dict)
		return results[::-1]


	def _check_if_exists(self,results,new_res):


		for res in results:
			res_copy = list(res)
			is_same_element = False
			for x in new_res:
				item_index = next((idx for idx,val in enumerate(res_copy) if val==x),None)
				if item_index!=None:
					is_same_element=True
					res_copy.pop(item_index)
				else:
					is_same_element=False
					break

			if is_same_element:
				return True

		return False


def main():
	sol = Solution()
	S = [2,-4,-5,-2,-3,-5,0,4,-2]
	res = sol.fourSum(S,-14)
	print(res)

if __name__ == '__main__':
	main()



# Not a good one!!
# ####################################
# class Solution(object):
# 	def fourSum(self, nums, target):
# 		meta_dict = {}
# 		results = []
# 		for x in nums:
# 			if not meta_dict:
# 				meta_dict[(x,)] = target-x
# 				continue
# 			temp = {}
# 			for key,val in meta_dict.items():
# 				if len(key)==3:
# 					if val==x:
# 						t = list(key)
# 						t.append(x)
# 						if not self._check_if_exists(results,t):
# 							results.append(t)
# 				elif len(key) < 3:
# 					t = list(tuple(key))
# 					t.append(x)
# 					temp[tuple(t)] = val-x

# 			meta_dict.update(temp)
			
# 			meta_dict[(x,)] = target-x

# 			# print(meta_dict)
# 		return results[::-1]


# 	def _check_if_exists(self,results,new_res):


# 		for res in results:
# 			res_copy = list(res)
# 			is_same_element = False
# 			for x in new_res:
# 				item_index = next((idx for idx,val in enumerate(res_copy) if val==x),None)
# 				if item_index!=None:
# 					is_same_element=True
# 					res_copy.pop(item_index)
# 				else:
# 					is_same_element=False
# 					break

# 			if is_same_element:
# 				return True

# 		return False



# def main():
# 	sol = Solution()
# 	S = [2,-4,-5,-2,-3,-5,0,4,-2]
# 	res = sol.fourSum(S,-14)
# 	print(res)

# if __name__ == '__main__':
# 	main()




