class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen=defaultdict(int)
        for i in range(len(numbers)):
            t=target - numbers[i]
            if seen[t]:
                return [seen[t],i+1]
            seen[numbers[i]]=i+1
        return []