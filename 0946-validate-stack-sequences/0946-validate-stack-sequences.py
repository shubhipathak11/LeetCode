class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        j = 0
        
        for i in pushed:
            stack.append(i)
            
            while len(stack) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                
        if len(stack):
            return False
        return True 
    
        # return not stack