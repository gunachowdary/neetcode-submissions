class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for name in strs:
            key = "".join(sorted(name))
            if key in group:
                group[key].append(name)
            else:
                group[key] = [name]
        return list(group.values())

solution = Solution()
result = solution.groupAnagrams(["act","pots","tops","cat","stop","hat"])
print(result)




        