class Solution:
    from collections import defaultdict
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lmult = 1
        rmult = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n
        for i in range(n):
            j = n - i - 1
            l_arr[i] = lmult
            r_arr[j] = rmult
            lmult *= nums[i]
            rmult *= nums[j]

        result = []
        for i in range(len(l_arr)):
            l = l_arr[i]
            r = r_arr[i]
            result.append(l*r)
        return result