class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            word = [0] * 26
            for char in s:
                word[ord(char) - ord('a')] += 1
            group[tuple(word)].append(s)
        
        return list(group.values())