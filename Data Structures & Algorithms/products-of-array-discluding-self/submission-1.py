class Solution:
    from collections import defaultdict
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = defaultdict(int)
        for i in range(len(nums)):
            mul = 1
            for j in range(len(nums)):
                if i != j:
                    mul *= nums[j]
            out[i] = mul
        return list(out.values())


        