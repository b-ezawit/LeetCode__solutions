class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [val for val in range(1,n+1)]  


        def soln(arr,count,start):
            if len(arr) == 1:
                return arr[0]  
            remove_indx = (start + count -1)%len(arr)
            arr.pop(remove_indx)
            return soln(arr,count,remove_indx)
        return soln(nums,k,0)


        

        


        
        