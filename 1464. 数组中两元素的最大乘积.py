class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if (nums[i] - 1) * (nums[i + j + 1] - 1) > sum:
                    sum = (nums[i] - 1) * (nums[i + j + 1] - 1)
        return sum