class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        
        target = Counter(s1)
        window = Counter(s2[:s1_len])

        if s1_len > s2_len:
            return False
        
        if target == window:
            return True
        
        for char in range(s1_len, s2_len):
            newchar = s2[char]
            window[newchar] += 1

            outchar = s2[char - s1_len]
            window[outchar] -= 1

            if window[outchar] == 0:
                del window[outchar]
            if target == window:
                return True
        return False
