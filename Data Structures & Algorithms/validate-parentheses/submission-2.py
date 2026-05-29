class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {'}': '{', ')': '(', ']': '['}

        for char in s:
            if char in paren:
                if not stack or stack.pop() != paren[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0