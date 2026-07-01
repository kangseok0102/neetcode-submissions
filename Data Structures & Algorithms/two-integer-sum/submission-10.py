class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for num in range(len(nums)):
            remain = target - nums[num]
            if remain in seen:
                return [seen[remain], num]
            seen[nums[num]] = num
