class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,v in enumerate(nums):
            print(i)
            c=target-nums[i]
            if c in seen:
                return [seen[c],i]
            seen[nums[i]]=i
        return []