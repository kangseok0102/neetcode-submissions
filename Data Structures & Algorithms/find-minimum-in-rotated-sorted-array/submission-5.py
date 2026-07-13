class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num = nums[0]

        for num in range(1, len(nums)):
            min_num = min(min_num, nums[num])

        return min_num

