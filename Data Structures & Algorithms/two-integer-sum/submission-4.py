class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            remain = target - nums[i]

            if remain in seen:
                return [seen[remain], i]
            
            else:
                seen[nums[i]] = i
        