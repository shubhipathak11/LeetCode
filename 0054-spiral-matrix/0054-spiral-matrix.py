class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        res = []
        
        left = 0
        right = n - 1
        
        top = 0
        bottom = m - 1
        
        while top <= bottom and left <= right:
            #Traverse top row.
            for col in range(left,right+1):
                res.append(matrix[top][col])
            
            top += 1
            
            #Traverse right column.
            for row in range(top,bottom+1):
                res.append(matrix[row][right])
            
            right -= 1
            
            if top <= bottom:
                for col in range(right,left-1,-1):
                    res.append(matrix[bottom][col])
                    
                bottom -= 1 
                
            if left <= right:
                for row in range(bottom,top-1,-1):
                    res.append(matrix[row][left])
                    
                left += 1
                
        return res