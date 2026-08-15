class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        a=[]
        
        def dfs(c,used):
            if len(c)==len(nums):
                a.append(c.copy())
                return
            for i in range(len(nums)):
                if used[i]==False:
                    used[i]=True
                    c.append(nums[i])
                    dfs(c,used)
                    c.pop()
                    used[i]=False
                
        used=[False]*len(nums)
        c=[]

        dfs(c,used)

        

        return a
                

