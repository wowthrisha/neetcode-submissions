from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l=1
        r=max(piles)
        k=r
        while l<=r:
            a=0
            m=(l+r)//2
            for i in range(len(piles)):
                a=a+ceil(piles[i]/m)
            print(piles[i],a)
            if a<=h:
                k=min(k,m)
                r=m-1
            else :
                l=m+1
        return k
