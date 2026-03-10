class RecentCounter(object):

    def __init__(self):
        self.requests = []
        self.start = 0


    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.start<len(self.requests) and t-self.requests[self.start] > 3000:
            self.start += 1
        self.requests.append(t)
        return len(self.requests) - self.start
            


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)