class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        #using counting sort:
        hmap = {}
        for i in range(len(heights)):
            hmap[heights[i]] = names[i]
        #hmap = {180:'Marry' , 165:'Jhon' , 170:'Emma'}
        count = [0] * (max(heights)+1)
        for n in heights:
            count[n] += 1
     
        ans = []
        for i in range(len(count)-1,-1,-1):
            while count[i] > 0:
                ans.append(hmap[i])
                count[i] -= 1
        
        return ans


 
