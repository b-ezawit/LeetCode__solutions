class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''
         all the elements are permutations from 1 to n--unique, 
        when sorted, each element in the array has its corresponding index at that element-1
        '''
        res = []
        n = len(arr)
        for curr_max in range(n,0,-1):
            indx = arr.index(curr_max)
            #if it is in its correct position, no need to make any flips
            if indx == curr_max -1:
                continue

            #if then indx == 0, we can't make left flip
            #only in indx > 0, left side flip is possible
            if indx != 0:
                res.append(indx+1)#left flip is made until indx+1--exclusive
                arr[:indx+1] = arr[:indx+1][::-1]
            res.append(curr_max)#right flip is made until the index of value curr_max
            arr[:curr_max] = arr[:curr_max][::-1]
        return res



            


        