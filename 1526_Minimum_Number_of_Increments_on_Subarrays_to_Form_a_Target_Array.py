class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        
        
        #count = initial amount of operations 
        count = target[0]
        for i, j in zip(target, target[1:]):
            if i < j:
                #sums up the difference of 2 elements
                count += j - i
        return count