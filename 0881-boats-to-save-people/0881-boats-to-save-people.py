class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()

        #[1,2,4,5]  l=2 r=2 boats=2
        #lim = 6
        l = 0
        r = len(people)-1
        boats = 0
        while l<r:
            if people[r]+people[l]<=limit:
                l += 1
                r -= 1
            else:
                r -= 1
            boats += 1
        
        if l== r:
            return boats+1
        else:
            return boats


        