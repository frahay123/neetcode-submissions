class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n):
            if nums[i] > 0: 
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo, hi = i+1, n-1
            while lo < hi:
                cur_sum = nums[lo] + nums[hi] + nums[i]
                if cur_sum == 0:
                    answer.append([nums[lo],nums[hi],nums[i]])
                    lo, hi = lo +1, hi-1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -=1
                elif cur_sum > 0:
                    hi -= 1
                else:
                    lo += 1
        return answer
