class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        master_map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            master_map[tuple(count)].append(s)
        
        return list(master_map.values())
