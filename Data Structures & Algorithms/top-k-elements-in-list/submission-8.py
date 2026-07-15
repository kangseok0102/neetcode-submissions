class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        for num, cnt in seen.items():
            bucket[cnt].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res