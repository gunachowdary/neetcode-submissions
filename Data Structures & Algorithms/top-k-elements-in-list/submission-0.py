class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for element in nums:
            if element in freq:
                freq[element] += 1
            else:
                freq[element] = 1

        return sorted(freq, key=freq.get, reverse=True)[:k]


solution = Solution()

result = solution.topKFrequent([1, 2, 2, 3, 3, 3], 2)

print(result)