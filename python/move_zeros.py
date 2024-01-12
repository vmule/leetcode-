class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        https://leetcode.com/problems/move-zeroes/
        """

        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
