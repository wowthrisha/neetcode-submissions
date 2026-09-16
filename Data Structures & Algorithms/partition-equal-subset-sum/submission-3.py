class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 != 0:
            return False

        target = s // 2

        def dfs(i, current_sum):
            if current_sum == target:
                return True

            if current_sum > target or i == len(nums):
                return False

            # Take nums[i]
            if dfs(i + 1, current_sum + nums[i]):
                return True

            # Don't take nums[i]
            if dfs(i + 1, current_sum):
                return True

            return False

        return dfs(0, 0)