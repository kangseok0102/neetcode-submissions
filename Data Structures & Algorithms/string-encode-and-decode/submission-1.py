class Solution:

    def encode(self, strs: List[str]) -> str:
        c_str = "".join(f"{len(s)}^{s}" for s in strs)
        return c_str

    def decode(self, s: str) -> List[str]:
        res, left = [], 0

        while left < len(s):
            right = left
            while s[right] != '^':
                right += 1
            length = int(s[left:right])
            start = right + 1
            res.append(s[start:start+length])

            left = start + length
        return res 
