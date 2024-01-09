class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        #creating set of nums paramas
        nums_set = set(nums)
        missing_num = 1
        
        #iterating from the first positive number '1'
        while missing_num in nums_set:
            missing_num += 1
        return missing_num