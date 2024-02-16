class Solution:
    def isValid(self, s: str) -> bool:
        
        map = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack =[]
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if stack[-1] == map[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0