class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            key_val = [0] * 26
            for c in s:
                key_val[ord(c) - ord('a')] += 1
            group[tuple(key_val)].append(s)
        
        return list(group.values())