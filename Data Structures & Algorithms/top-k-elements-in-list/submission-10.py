class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for num in range(len(nums)):
            count[nums[num]] = count.get(nums[num], 0) + 1

        for num, cnt in count.items():
            bucket[cnt].append(num)

        res = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res 
