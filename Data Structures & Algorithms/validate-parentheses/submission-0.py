class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CloseToOpen = {")" : "(", "]" : "[", "}" : "{"}

        # Go through every char in string
        for c in s:
            # If it is a closing paranthesis (key)
            if c in CloseToOpen:
                if stack and stack[-1] == CloseToOpen[c]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)

        return True if not stack else False

