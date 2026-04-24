class Node:
    def __init__(self,val,next,prev):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(val=homepage,next=None,prev=None)
        self.back_elements = 0
        self.front_elements = 0
        
                

    def visit(self, url: str) -> None:
        newNode = Node(val=url,next=None,prev=self.curr)
        self.curr.next = newNode
        self.curr = newNode
        self.front_elements = 0
        self.back_elements += 1
       
        
        #leetcode.com->google.com->facebook.com->youtube.com
        #front = 0
        #back = 3

    def back(self, steps: int) -> str:

        #leetcode.com->google.com->facebook.com->youtube.com
        #back(1)
        #0
        if self.back_elements == 0:
            return self.curr.val
      
        for _ in range(min(steps,self.back_elements)):
            self.curr = self.curr.prev
            self.back_elements -= 1
            self.front_elements += 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        if self.front_elements == 0:
            return self.curr.val

        for _ in range(min(steps,self.front_elements)):
            self.curr =  self.curr.next
            self.back_elements += 1
            self.front_elements -= 1
        return self.curr.val



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)