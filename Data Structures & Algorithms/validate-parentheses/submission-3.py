class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")" : "(", "]" : "[", "}" : "{"}

        for char in s: 
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack or stack.pop() != pairs[char]:
                    return False
            # ignore any other characters, if present)

        return not stack # True only if everything was matched

        

