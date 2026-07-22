class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = 0
        r_wall = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = n - i - 1
            max_left[i] = l_wall
            max_right[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
        total_water = 0
        for i in range(n):
            max_water = min(max_left[i], max_right[i])
            total_water += max(0,max_water - height[i])

        return total_water