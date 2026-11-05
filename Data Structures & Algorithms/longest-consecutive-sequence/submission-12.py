class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in num_set:
            if num - 1 in num_set:
                continue

            current_num = num
            streak = 1
            
            while current_num + 1 in num_set:
                streak += 1
                current_num += 1
            max_len = max(max_len, streak)
        
        return max_len
                