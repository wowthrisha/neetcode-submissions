class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, remaining):
            if remaining == 0:
                res.append(cur.copy())
                return

            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break

                cur.append(nums[i])
                dfs(i, remaining - nums[i])   # reuse allowed
                cur.pop()

        cur = []
        dfs(0, target)
        return res