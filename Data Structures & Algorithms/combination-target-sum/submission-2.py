class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        a=[]
        nums.sort()   
        def dfs(start,r):
            if r==0:
                a.append(c.copy())
                return
            
            for i in range(start,len(nums)):
                if r<nums[i]:
                    break
                c.append(nums[i])
                dfs(i,r-nums[i])
                c.pop()
        c=[]
        dfs(0,target)
        return a
