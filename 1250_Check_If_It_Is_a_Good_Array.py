import math

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool: 
        #all we have to see is if there is a combination with gcd = 1
        d = nums[0]
        for num in nums:
            d = math.gcd(num, d)
        return d == 1
    

# Bézout's identity:  gcd(a,b) = d  ->  f(x,y) | ax + by = d
# https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity

    