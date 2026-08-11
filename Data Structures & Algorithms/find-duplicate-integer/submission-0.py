class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        b=0
        while b!=slow:
            slow=nums[slow]
            b=nums[b]
        return b
        
        

