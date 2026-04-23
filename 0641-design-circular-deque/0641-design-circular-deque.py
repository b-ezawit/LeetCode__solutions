class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k =  k
        self.d = deque(maxlen=self.k)
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        self.d.appendleft(value)
        if self.d[0] == value:
            return True
        else:
            return False

        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.d.append(value)

        if self.d[-1] == value:
            return True 
        else:
            return False
    
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.d.popleft()
            return True
            


    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.d.pop()
            return True


    def getFront(self):
        """
        :rtype: int
        """
        if not self.d:
            return -1
        else:
            return self.d[0]
        

    def getRear(self):
        """
        :rtype: int
        """
      
        if not self.d:
            return -1
        else:
            return self.d[-1]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if not self.d:
            return True
        else:
            return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.d)==self.k:
            return True
        else:
            return False
        

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()