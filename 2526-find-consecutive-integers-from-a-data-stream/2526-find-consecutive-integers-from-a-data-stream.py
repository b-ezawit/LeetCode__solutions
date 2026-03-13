class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.nums = deque()
        self.value = value
        self.k = k


        

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num != self.value:
            self.nums.clear()
        else:
            self.nums.append(num)
        
        if len(self.nums) > self.k:
            self.nums.popleft()
        
        return len(self.nums) == self.k


        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)