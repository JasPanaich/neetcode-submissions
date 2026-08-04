class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # Track min element at each step
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # Need to duplicate the value that was already there 
            self.min_stack.append(self.min_stack[-1])
        
    def pop(self) -> None:
        self.stack.pop()
        
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # Keep track as we append list so its O(1) time complexity
        return self.min_stack[-1]

    
        
