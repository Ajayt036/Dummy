class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rep = list(set([i for i in nums if nums.count(i)>1])) 
        rep
        
        Index_list = []
        for k in rep:
            Index_list.append([i for i,v in enumerate(nums) if v == k])
        Index_list
        
        return(sum([(len(i)*(len(i)-1)/2) for i in Index_list]))