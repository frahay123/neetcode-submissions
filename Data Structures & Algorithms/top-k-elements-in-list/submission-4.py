class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        k_terms = []
        for i in range(k):
            max_freq = -1 
            term = 0
            for num in freq:
                if freq[num] > max_freq:
                    max_freq = freq[num]
                    term = num
            freq[term] = 0
            k_terms.append(term)
        
        return k_terms
