class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [n for n in range(1,n+1)]
        def soln(arr,k,start):
            if len(arr) == 1:
                return arr[0]
            remove_indx = (start+k-1) % len(arr)
            arr.pop(remove_indx)

            return soln(arr,k,remove_indx)   
        return soln(nums,k,0)         


        

        


        
        