class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums) #largest number in the nums array
        right = sum(nums)#the sum of the values in the nums array
        
        #def to check if the sum of the subarrays is bigger than the middle
        def numberOfGroups(large: int) -> int:
            count_for_groups = 1 #inital counter to 1 because minimum size of subarrays is one
            sum_in_each_group = 0 #init sum to zero
            # for each number in our array
            for num in nums:
                check = sum_in_each_group + num #check what is our num plus the funal sum
                if check <= large: #if it's smaller than the larger num in the array
                    sum_in_each_group += num #we add the number to sum 
                else:
                    count_for_groups += 1 #than we need a new group 
                    sum_in_each_group = num #put the num of the new group in the sum
            return count_for_groups #return number of groups
        
        
        # this is where the binary search starts
        while left < right: #classic for binary search
            middle = (right + left) // 2 # find the mid search
            if numberOfGroups(middle) > m: #check that number of groups is not bigger than 'm'
                left = middle + 1 #if it is bigger than we move 'left'
            else:
                right = middle #if it is smaller or equal than we move 'right'
        return left #return the left because it is the minimize large sum we finally found! :)
        