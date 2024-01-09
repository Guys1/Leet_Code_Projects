class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0

        res = 0
        #running through array height both ends
        while left < right:
            #
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            #calculating left amount as long as left max is smaller then right max
            if left_max < right_max:
                res += left_max - height[left]
                #advancing left side by 1
                left+=1
            #calculating right amount as long as right max is smaller then left max
            else: 
                res += right_max - height[right]
                #regresing right side by 1
                right-=1

        return res