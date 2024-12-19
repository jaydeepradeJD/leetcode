class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ptr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[ptr-1]:
                continue
            else:
                nums[ptr] = nums[i]
                ptr += 1
        return ptr