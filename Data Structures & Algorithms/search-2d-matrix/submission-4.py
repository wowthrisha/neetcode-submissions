class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr=len(matrix)
        nc=len(matrix[0])
        for r in range(nr):
            print("r=",r)
            if matrix[r][0]==target or matrix[r][-1]==target:
                    return True
            elif matrix[r][0]<target and matrix[r][-1]>target:

                print("hi",r)
                p,q=0,nc-1
                while p<=q:
                    m=(p+q)//2
                    if matrix[r][m]==target:
                        return True
                    elif matrix[r][m]<target:
                        p=m+1
                    else:
                        q=m-1
            
        return False
        

