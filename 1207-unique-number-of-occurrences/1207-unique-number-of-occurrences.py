class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        res=[]
        f=0
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return len(set(d.values()))==len(d.values())