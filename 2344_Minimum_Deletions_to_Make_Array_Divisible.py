class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gcd = reduce(math.gcd, numsDivide)

        #sorting 'nums' and kepping track over every element index
        #find out who is the smallest element 'nums[i]' in 'nums' that divides gcd
        for i, num in enumerate(sorted(nums)):
            #checking if the element 'nums[i]' divides gcd
            if gcd % num == 0:
                return i

        return -1