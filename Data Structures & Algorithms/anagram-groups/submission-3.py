class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            
            #alpha order
            sorted_s = sorted(s)
            sorted_string = ''.join(sorted_s)
            #bring to intermediate form by ordering =mapping
            if sorted_string not in d:
                d[sorted_string] = [s]
            else:
                d[sorted_string].append(s)
        
        return list(d.values())
