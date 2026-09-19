class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        m=[-1]*n
        def dfs(i):
            if m[i]!=-1:
                return m[i]
            lis=1
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    
                    lis=max(lis,1+dfs(j))
                    m[i]=lis
                    
                    
            return lis
        
        l=0
        for i in range(n):
            l=max(l,dfs(i))
        return l
    

            