class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for num in range(len(numbers)):
            remain = target - numbers[num]
            if remain in seen:
                return [seen[remain] + 1, num + 1]
            
            seen[numbers[num]] = num
        