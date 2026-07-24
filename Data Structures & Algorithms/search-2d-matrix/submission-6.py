class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ro=len(matrix)
        co=len(matrix[0])
        l,r=0,ro*co-1
        while l<=r:
            m=(l+r)//2
            ri=m//co
            ci=m%co
            a=matrix[ri][ci]
            if a==target:
                return True
            elif a<target:
                l=m+1
            else:
                r=m-1
        return False