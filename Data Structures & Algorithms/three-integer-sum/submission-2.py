class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        #[-4, -1, -1, 0, 1, 2]
        for num in range(len(nums) - 2):
            if num > 0 and nums[num] == nums[num - 1]:
                continue
            if nums[num] > 0:
                break
            
            left, right = num + 1, len(nums) - 1
            while left < right:
                total = nums[num] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[num], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
        return res


