# Given an array of integers, return indices of the two
# numbers such that they add up to a specific target.

# You may assume that each input would have exactly one 
# solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#####################################
# O(N) time complexity solution

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp_dict = {} # as simple as using a dict!
        for i in range(len(nums)):
            if nums[i] in temp_dict:
                return [temp_dict[nums[i]],i]
            else:
                temp_dict[target-nums[i]] = i

def main():
    s = Solution()
    print(s.twoSum([3,2,4],6))


if __name__=="__main__":
    main()