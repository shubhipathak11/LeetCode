class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        
        nums.sort()
        
        for i in range(len(nums)):
            l = i+1 
           
            r = len(nums)-1
            
            while l < r:
                
                if nums[l] + nums[r] + nums[i] == 0:
                    val = [nums[i],nums[l],nums[r]]
                    s.add(tuple(val))
                    l += 1
                    r -= 1
                
                else:
                    if nums[i] + nums[l] + nums[r] > 0:
                        r -= 1
                    else:
                        l += 1 
        return s
                    
        