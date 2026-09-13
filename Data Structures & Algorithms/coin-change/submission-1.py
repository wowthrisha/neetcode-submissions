class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
     
        #dp array with amount+1 values, initialised to amount+1 to satisfy min()
        dp=(amount+1)*[amount+1]
        dp[0]=0
        for t in range(1,amount+1):
            for c in coins:
                if c<=t:
                    dp[t]=min(dp[t],dp[t-c]+1)
        if dp[amount]==amount+1:
            return -1
            
            
                
                
        return dp[amount]
        
