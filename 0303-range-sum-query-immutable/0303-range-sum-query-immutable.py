class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.pref = []
        _sum = 0
        for n in nums:
            _sum += n
            self.pref.append(_sum)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.pref[right]
        return self.pref[right] - self.pref[left-1]


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)