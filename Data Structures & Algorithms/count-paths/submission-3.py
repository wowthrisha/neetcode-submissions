class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d={}
        def dfs(i,j):
            if (i,j) in d:
                return d[(i,j)]
            if i>m-1 or j>n-1:
                return 0
            if i==m-1 and j==n-1:
                return 1
            p=dfs(i,j+1)+dfs(i+1,j)
            d[(i,j)]=p
            
            return dfs(i,j+1)+dfs(i+1,j)
        return dfs(0,0)