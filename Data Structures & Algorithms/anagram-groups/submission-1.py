class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            key = "".join(sorted(word))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        return list(anagrams.values())
sol = Solution()
result = sol.groupAnagrams(["act","pots","tops","cat","stop","hat"])
print(result)