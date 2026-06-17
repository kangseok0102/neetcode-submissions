class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {'}':'{', ']':'[', ')':'('}

        for char in s:
            if char in paren:
                if not stack or paren[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0