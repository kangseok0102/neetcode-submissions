class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = max(nums)

        for num in range(len(nums)):
            min_num = min(min_num, nums[num])

        return min_num