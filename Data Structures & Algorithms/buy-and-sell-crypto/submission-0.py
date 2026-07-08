class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=0
        l=prices[0]
        for i in range(len(prices)):
            if prices[i]<l:
                l=prices[i]
            else:
                mp=max(mp,prices[i]-l)
        return mp