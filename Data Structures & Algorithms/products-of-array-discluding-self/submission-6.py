class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        left_product = 1
        for num in range(len(nums)):
            ans[num] = left_product
            left_product *= nums[num]
        
        right_product = 1
        for num in range(len(nums)-1, -1, -1):
            ans[num] *= right_product
            right_product *= nums[num]
        
        return ans
