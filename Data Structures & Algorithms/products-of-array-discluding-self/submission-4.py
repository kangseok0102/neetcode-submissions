class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        ans = [1] * len(nums)

        left_product = 1
        for num in range(len(nums)):
            ans[num] = left_product
            left_product *= nums[num]
        
        right_product = 1
        for num in range(len(nums) - 1, -1, -1):
            ans[num] *= right_product
            right_product *= nums[num]

        return ans