class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq_set = set()

        for num in nums:
            if num in uniq_set:
                return True
            
            uniq_set.add(num)
        
        return False
