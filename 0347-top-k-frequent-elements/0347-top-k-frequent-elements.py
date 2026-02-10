class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_count = Counter(nums)
        return [val for val,freq in nums_count.most_common(k)]
