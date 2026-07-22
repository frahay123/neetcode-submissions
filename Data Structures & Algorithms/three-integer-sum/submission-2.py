class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)-1
        num_ans = []

        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo, hi = i+1, n
            while lo < hi:
                ans = nums[i] + nums[lo] + nums[hi]
                if ans == 0:
                    num_ans.append([nums[i],nums[lo], nums[hi]])
                    lo+=1
                    hi-=1
                    while lo < hi and nums[lo-1] == nums[lo]:
                        lo+=1
                    while lo < hi and nums[hi+1] == nums[hi]:
                        hi-=1
                elif ans > 0:
                    hi-=1
                else:
                    lo+=1
        return num_ans