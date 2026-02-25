class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        

        #ssss , mmmm, llll --3n and each of u can take the same number finally
        #for me to get max numberof coins i must not touch the small, i pick s,m,l for bob to take all the smalls
        piles.sort()
        res = 0
        #[2,4,1,2,7,8]
        #piles = [1,2,   2,4,7,8]
        div = len(piles)/3 #div = 2

        #ss mm ll
        i = div
        while i <len(piles):
            res += piles[i]
            i += 2
        
        return res
            

        
        